features = []


def register_feature(name):
    def _register_feature(func):
        features.append({'name': name, 'class': func})
        return func
    return _register_feature
