import time

import telethon

import service.service
import utils.utils


@service.service.register_main_thread_feature('news')
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
            if '#крипто' in event.text and not event.photo:
                text = event.text.replace('**', '').replace('__', '')
                status = 0
                to_be_replaced = ''
                data = ''
                for char in text:
                    if status == 0 and char == '[':
                        to_be_replaced += '['
                        status = 1
                    elif status == 1 and char != ']':
                        data += char
                    elif status == 1 and char == ']':
                        to_be_replaced += data + ']'
                        status = 2
                    elif status == 2 and char == '(':
                        status = 3
                        to_be_replaced += '('
                    elif status == 3 and char != ')':
                        to_be_replaced += char
                    elif status == 3 and char == ')':
                        to_be_replaced += ')'
                        text = text.replace(to_be_replaced, data)
                        status = 0
                        to_be_replaced = ''
                        data = ''
                self.app.client.method('wall.post', message=text)

    def run(self):
        pass

    def start(self):
        self.client.start()
        self.client.run_until_disconnected()
