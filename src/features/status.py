import datetime
import time

import requests

import service.service
import utils.utils


@service.service.register_feature('status')
class StatusFeature:
    def __init__(self, app):
        self.app = app

    def _get_price(self):
        return requests.get(
            'https://api.coingecko.com/api/v3/simple/price'
            '?ids=ethereum,bitcoin&vs_currencies=usd'
        ).json()

    def _get_datetime(self):
        try:
            # unix
            return datetime.datetime.utcnow().strftime('%-m/%-d %-I:%M %p')
        except ValueError:
            # windows
            return datetime.datetime.utcnow().strftime('%#m/%#d %#I:%M %p')

    def _format(self, value):
        return '{:,}'.format(int(value))

    @utils.utils.asynchronous
    def run(self):
        while self.app.running:
            try:
                price = self._get_price()
                status = (
                    f'🚀 BTC: ${self._format(price["bitcoin"]["usd"])}; '
                    f'ETH: ${self._format(price["ethereum"]["usd"])} | '
                    f'🕓 Last update: {self._get_datetime()} UTC'
                )
                self.app.client.method('status.set', text=status)
            except Exception:
                pass
            time.sleep(60)
