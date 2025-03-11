# Copyright (C) 2016-2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import asyncio
import logging
import os
import threading
import time
from queue import Empty
from typing import Any
from typing import Coroutine
from typing import Iterable

from aorta.types import Acknowledgable
from aorta.types import Envelope
from aorta.types import IMessageHandler
from aorta.types import IPool


class Worker(threading.Thread):
    interval: float = 1
    logger: logging.Logger = logging.getLogger('aorta.transport')
    must_exit: bool = False
    tasks: set[asyncio.Task[None]]

    def __init__(self, pool: IPool, limit: int):
        self.limit = limit
        self.pool = pool
        self.worker_id = bytes.hex(os.urandom(24))
        super().__init__(
            target=lambda: asyncio.run(self.main_event_loop()),
            daemon=True
        )
        self.start()

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

    def join(self, timeout: float | None = None):
        self.stop()

    def main_event(self) -> None:
        if len(self.tasks) >= self.limit:
            return
        while len(self.tasks) < self.limit:
            try:
                frame, envelope, handlers = self.pool.get()
                self.create_task(self.execute(frame, envelope, handlers))
            except Empty:
                break

    def on_task_completed(
        self,
        task: asyncio.Task[Any],
        envelope: Envelope[Any],
    ) -> None:
        pass

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
        return await self.runner.run(
            publisher=self.publisher,
            envelope=envelope,
            handlers=handlers
        )