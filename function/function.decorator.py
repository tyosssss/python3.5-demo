# conding=utf-8
from functools import reduce, wraps


def log_cost_time(func):
    @wraps(func)
    def wrapper(*args, **kargs):
        import time
        begin = time.time()
        try:
            return func(*args, **kargs)
        finally:
            print('func %s cost %s' % (func.__name__, time.time() - begin))

    return wrapper


@log_cost_time
def sum(*args, **kargs):
    return reduce(lambda s, x: s + x, list(args) + list(kargs.values()))