# Copyright (C) 2016-2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import os
from typing import TYPE_CHECKING

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
        prefetch: int = 1
    ):
        super().__init__(pool)
        self.prefetch = prefetch

    def main_event(self) -> None:
        if self.must_exit:
            return
        response = self.subscriber.pull(  # type: ignore
            subscription=self.subscription_id,
            max_messages=self.prefetch,
            return_immediately=True
        )
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
            subscription=self.subscription_id,
            ack_ids=ack_ids
        )

    def configure(self) -> None:
        super().configure()
        self.subscription_id = os.environ['GOOGLE_PUBSUB_SUBSCRIPTION']
        self.subscriber = SubscriberClient()
        self.logger.debug("Established connection to subscription %s", self.subscription_id)