import features
import service.service


class Application:
    def __init__(self, **kwargs):
        self.classes = {}
        self.features = {}
        self.main_thread_features = {}

        for key, value in kwargs.items():
            self.classes[key] = value
            setattr(self, key, value)

        for _feature in service.service.features:
            func = _feature['class'](self)
            self.features[_feature['name']] = func
            setattr(self, _feature['name'], func)
        
        for _feature in service.service.main_thread_features:
            func = _feature['class'](self)
            self.main_thread_features[_feature['name']] = func
            setattr(self, _feature['name'], func)

        self.running = True

        for _feature in self.features.values():
            _feature.run()
        
        for _feature in self.main_thread_features.values():
            _feature.start()
