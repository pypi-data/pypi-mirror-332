# Copyright (C) 2016-2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import asyncio
import contextlib
import logging
import os
import threading
import time
from typing import Any
from typing import Coroutine
from typing import Iterable

from aorta.types import Acknowledgable
from aorta.types import Envelope
from aorta.types import IMessageHandler
from aorta.types import IPool
from aorta.provider import Provider


class Worker(threading.Thread):
    interval: float = 1
    logger: logging.Logger = logging.getLogger('aorta.transport')
    must_exit: bool = False
    running: int = 0
    tasks: set[asyncio.Task[None]]

    def __init__(self, pool: IPool):
        self.pool = pool
        self.worker_id = bytes.hex(os.urandom(24))
        super().__init__(
            target=lambda: asyncio.run(self.main_event_loop()),
            daemon=True
        )
        self.start()

    def accept_message(self, frame: Acknowledgable):
        if self.must_exit or self.loop.is_closed():
            # Do not use an async call here.
            self.reject(frame)
            return
        self.pool.notify(frame)
        envelope = None
        try:
            envelope = Provider.loads(frame.data)
            if envelope is None:
                raise ValueError("Unable to parse message from incoming data.")
        except Exception as e:
            self.acknowledge(frame)
            self.logger.warning("Caught fatal %s", repr(e))
            return
        assert envelope is not None
        if isinstance(envelope, Envelope):
            self.on_message_received(frame, envelope) # type: ignore
        else:
            self.reject(frame)
            self.logger.warning(
                "Received unknown Aorta message (kind: %s, uid: %s, id: %s)",
                envelope.kind,
                envelope.metadata.uid[:6],
                envelope.metadata.correlation_id[:6]
            )

    def acknowledge(self, frame: Acknowledgable):
        try:
            frame.ack()
            self.logger.debug("Accepted message %s", frame.message_id)
        except Exception as e:
            self.on_acknowledge_failure(frame, e)

    def create_task(self, c: Coroutine[Any, Any, Any]):
        if self.loop.is_closed():
            self.logger.critical(
                "Received a task on closed event loop."
            )
            return
        task = self.loop.create_task(c)
        self.tasks.add(task)
        return task

    def configure(self) -> None:
        self.loop = asyncio.get_event_loop()
        self.tasks = set()

    @contextlib.contextmanager
    def event_loop(self, envelope: Envelope[Any]):
        try:
            yield self.loop
        except Exception as e:
            self.logger.exception(
                "Caught fatal %s while handling message (uid: %s, correlation-id: %s)",
                type(e).__name__,
                envelope.metadata.uid,
                envelope.metadata.correlation_id
            )
            return True

    def join(self, timeout: float | None = None):
        self.stop()

    def main_event(self) -> None:
        raise NotImplementedError

    def on_message_received(
        self,
        frame: Acknowledgable,
        envelope: Envelope[Any],
    ):
        self.logger.debug("Accepted message %s (kind: %s)", frame.message_id, envelope.kind)
        task = self.create_task(self.execute(frame, envelope, Provider.get(envelope)))
        if task is not None:
            self.running += 1
            task.add_done_callback(lambda t: self.on_task_completed(t, envelope))

    def on_acknowledge_failure(self, frame: Acknowledgable, exception: BaseException):
        self.logger.critical(
            "Failed to acknowledge message, redelivery might occur (id: %s, exception: %s)",
            frame.message_id,
            repr(exception)
        )

    def on_reject_failure(self, frame: Acknowledgable, exception: BaseException):
        self.logger.critical(
            "Failed to reject message, redelivery might occur (id: %s, exception: %s)",
            frame.message_id,
            repr(exception)
        )

    def on_task_completed(
        self,
        task: asyncio.Task[Any],
        envelope: Envelope[Any],
    ) -> None:
        self.running -= 1

    def reject(self, frame: Acknowledgable):
        try:
            frame.nack()
            self.logger.debug("Rejected message %s", frame.message_id)
        except Exception as e:
            self.on_reject_failure(frame, e)

    def stop(self):
        self.must_exit = True
        self.logger.info("Tearing down worker (id: %s)", self.ident)
        return self

    async def main_event_loop(self):
        self.logger.debug("Spawning worker (thread: %s)", self.ident)
        self.publisher = self.pool.get_publisher()
        self.runner = self.pool.get_runner(self.publisher)
        self.configure()
        self.logger.debug("Start polling for new messages (thread: %s)", self.ident)
        while True:
            # Check pending tasks before doing anything.
            try:
                self.main_event()
            except Exception as e:
                self.logger.exception(
                    "Caught fatal %s in main event.",
                    type(e).__name__
                )
            if self.tasks:
                done, *_ = await asyncio.wait(
                    fs=self.tasks,
                    timeout=0.1,
                    return_when='FIRST_COMPLETED'
                )
                for t in done:
                    self.tasks.remove(t)
            if self.must_exit:
                if self.tasks:
                    await asyncio.wait(self.tasks)
                break
            time.sleep(self.interval)

    async def execute(
        self,
        frame: Acknowledgable,
        envelope: Envelope[Any],
        handlers: Iterable[type[IMessageHandler]]
    ) -> None:
        try:
            return await self.runner.run(
                publisher=self.publisher,
                envelope=envelope,
                handlers=handlers
            )
        finally:
            self.acknowledge(frame)