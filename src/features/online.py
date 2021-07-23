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
            try:
                self.app.client.method('account.setOnline')
            except Exception:
                pass
            time.sleep(290)
