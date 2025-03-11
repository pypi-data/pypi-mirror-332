# Copyright (C) 2016-2025 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import logging
import logging.config
import time
from typing import Any
from typing import TypeVar

from libcanonical.runtime import MainProcess # type: ignore

from aorta import Command
from aorta import Event
from aorta import MessagePublisher
from aorta import NullTransport
from aorta.types import Acknowledgable
from aorta.types import Envelope
from aorta.types import IPublisher
from aorta.types import IRunner
from aorta.pool import ThreadWorker

E = TypeVar('E', bound=Command|Event)


class BaseConsumer(MainProcess):
    __module__: str = 'aorta.ext.consumer'
    concurrency: int = 1
    debug: bool = False
    interval = 0.25
    logger: logging.Logger = logging.getLogger('aorta.transport.ingress')
    max_messages: int = 0
    metrics: logging.Logger = logging.getLogger('aorta.metrics')
    num_workers: int = 1
    workers: list[ThreadWorker]

    def __init__(
        self,
        name: str,
        workers: int = 1,
        concurrency: int = 1,
        max_runtime: float = 0.0,
        max_messages: int = 0,
        loglevel: str = 'INFO',
        transport_loglevel: str = 'WARNING',
        **kwargs: Any
    ):
        super().__init__(name=name)
        self.concurrency = concurrency
        self.loglevel = loglevel
        self.max_runtime = max_runtime
        self.max_messages = max_messages
        self.max_workers = workers
        self.received = 0
        self.transport_loglevel = transport_loglevel
        self.workers = []

    def configure(self, reloading: bool = False):
        self.logger.debug("Running with %s workers", self.concurrency)
        if not reloading:
            self.publisher = self.get_publisher()
            for _ in range(self.max_workers):
                self.workers.append(self.initialize_worker())
        if self.max_messages:
            self.logger.info("Worker will consume at most %s messages", self.max_messages)

    def configure_worker(self) -> None:
        logging.config.dictConfig(dict(self.get_logging_config()))

    def get_publisher(self) -> IPublisher:
        return MessagePublisher(
            transport=NullTransport()
        )

    def get_runner(self, publisher: IPublisher) -> IRunner:
        raise NotImplementedError

    def initialize_worker(self) -> ThreadWorker:
        raise NotImplementedError

    def notify(self, frame: Acknowledgable):
        self.received += 1

    def route(self, envelope: Envelope[E]) -> list[str]:
        """Return a list of strings indicating the topics that the
        `envelope` must be sent to. Subclasses must override this
        method.
        """
        raise NotImplementedError

    def main_event(self) -> None:
        if self.max_messages:
            must_exit = any([
                self.received >= self.max_messages,
                self.max_runtime and (self.age > self.max_runtime) and self.received == 0
            ])
            if not must_exit:
                return

            self.logger.warning(
                "Received maximum amount of %s messages after %0.2fs, exiting.",
                self.received,
                self.age
            )
            self.stop()
            for worker in self.workers:
                worker.stop()
                self.logger.debug("Closing worker (id: %s)", worker.ident)
            t0 = time.monotonic()
            while any([w.is_alive() for w in self.workers]):
                time.sleep(1)
                dt = (time.monotonic() - t0)
                if dt > 180:
                    self.logger.warning("Workers did not stop after %.02f seconds.", dt)