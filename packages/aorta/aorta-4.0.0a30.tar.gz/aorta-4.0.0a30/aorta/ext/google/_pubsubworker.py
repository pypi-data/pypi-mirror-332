# Copyright (C) 2016-2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import time
import os
from typing import TYPE_CHECKING

from google.api_core.exceptions import InvalidArgument
from google.api_core.exceptions import NotFound
from google.cloud.pubsub_v1 import SubscriberClient # type: ignore
from google.cloud.pubsub_v1.subscriber.futures import StreamingPullFuture # type: ignore

from aorta.pool import ThreadWorker
from ._frame import Frame
if TYPE_CHECKING:
    from ._topiclistener import TopicListener


class PubsubWorker(ThreadWorker):
    streamer: StreamingPullFuture
    pool: 'TopicListener'

    def __init__(
        self,
        pool: 'TopicListener',
        *,
        project: str,
        subscription: str | None,
        prefetch: int = 1
    ):
        super().__init__(pool)
        self.prefetch = prefetch
        self.project = project
        self.subscription = subscription

    def main_event(self) -> None:
        if self.must_exit:
            return
        n = max(self.prefetch - self.running, 0)
        if n == 0:
            self.logger.debug("Suspending message pull (running: %s)", self.running)
            return
        try:
            response = self.subscriber.pull(  # type: ignore
                subscription=self.subscription,
                max_messages=self.prefetch,
                return_immediately=True
            )
            if not response.received_messages:
                return

            frames: list[Frame] = []
            ack_ids: list[str] = []
            for message in response.received_messages:
                frame = Frame(message)
                if not self.pool.can_accept():
                    break
                self.pool.notify(frame)
                ack_ids.append(message.ack_id)
                frames.append(frame)
                self.accept_message(frame)
            self.subscriber.acknowledge( # type: ignore
                subscription=self.subscription,
                ack_ids=ack_ids
            )
        except (InvalidArgument, NotFound) as e:
            self.logger.critical(e.message) # type: ignore
            time.sleep(5)

    def configure(self) -> None:
        super().configure()
        self.subscriber = SubscriberClient()
        if self.subscription is None:
            self.subscription = os.environ['GOOGLE_PUBSUB_SUBSCRIPTION']
        self.subscription = self.subscriber.subscription_path(self.project, self.subscription)
        self.logger.debug("Established connection to subscription %s", self.subscription)