import time

import service.service
import utils.utils


@service.service.register_feature('online')
class OnlineFeature:
    def __init__(self, app):
        self.app = app

    @utils.utils.asynchronous
    def run(self):
        while self.app.running:
            self.app.client.method('account.setOnline')
            time.sleep(300)
