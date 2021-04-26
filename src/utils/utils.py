import functools
import threading


def asynchronous(func):
    @functools.wraps(func)
    def asynchronous_func(*args, **kwargs):
        thread = threading.Thread(target=func, args=args, kwargs=kwargs)
        thread.daemon = True
        thread.start()
    return asynchronous_func
