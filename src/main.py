import time

import api.vk
import app
import default.config
import utils.config


def main():
    config = utils.config.Config(
        'config.json', default=default.config.DEFAULT
    )
    client = api.vk.Client(
        config.get('VK_API_TOKEN'),
        debug=config.get('DEBUG_MODE')
    )
    application = app.Application(config=config, client=client)

    while application.running:
        time.sleep(1)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Exiting...')
