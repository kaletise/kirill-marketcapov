import features
import service.service


class Application:
    def __init__(self, **kwargs):
        self.classes = {}
        self.features = {}

        for key, value in kwargs.items():
            self.classes[key] = value
            setattr(self, key, value)

        for _feature in service.service.features:
            func = _feature['class'](self)
            self.features[_feature['name']] = func
            setattr(self, _feature['name'], func)

        self.running = True

        for _feature in self.features.values():
            _feature.run()
