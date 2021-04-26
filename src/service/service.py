features = []
main_thread_features = []


def register_feature(name):
    def _register_feature(func):
        features.append({'name': name, 'class': func})
        return func
    return _register_feature


def register_main_thread_feature(name):
    def _register_main_thread_feature(func):
        main_thread_features.append({'name': name, 'class': func})
        return func
    return _register_main_thread_feature
