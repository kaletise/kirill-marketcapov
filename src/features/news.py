import time

import telethon

import service.service
import utils.utils


@service.service.register_feature('news')
class NewsFeature:
    def __init__(self, app):
        self.app = app

        self.client = telethon.TelegramClient(
            'marketcapov',
            self.app.config.get('TELEGRAM_APP_ID'),
            self.app.config.get('TELEGRAM_APP_HASH')
        )

        @self.client.on(telethon.events.NewMessage(chats='@markettwits'))
        async def news_handler(event):
            if '#крипто' in event.text:
                self.app.client.method('wall.post', message=event.text)

    def run(self):
        self.client.start()
        self.client.run_until_disconnected()
