import requests


class Client:
    def __init__(self, token, debug=False, version='5.130'):
        self.token = token
        self.debug = debug
        self.version = version
    
    def _method(self, name, **kwargs):
        return requests.post(
            f'https://api.vk.com/method/{name}',
            data={
                **kwargs, 'v': self.version, 'access_token': self.token
            }
        ).json()

    def method(self, name, **kwargs):
        response = self._method(name, **kwargs)
        if self.debug:
            print(name, response)
        return response
