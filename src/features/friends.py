import time

import service.service
import utils.utils


@service.service.register_feature('friends')
class FriendsFeature:
    def __init__(self, app):
        self.app = app

    @utils.utils.asynchronous
    def run(self):
        while self.app.running:
            requests = self.app.client.method('friends.getRequests')
            if requests.get('response'):
                for user_id in requests['response'].get('items'):
                    self.app.client.method(
                        'friends.add', user_id=user_id
                    )
                    time.sleep(10)
            time.sleep(15)
