import pickle
import hashlib
import time

# caching decorator
cache = {}


def is_obsolete(entry, duration):
    return time.time() - entry['time'] > duration


def compute_key(function, args, kw):
    key = pickle.dumps((function.func_name, args, kw))
    return hashlib.sha1(key).hexdigest()


# here is a decorator function itself
def memoize(duration=10):
    def _memoize(function):
        def __memoize(*args, **kw):
            key = compute_key(function, args, kw)

            # check if exists
            if key in cache and not is_obsolete(cache[key], duration):
                print 'winner'
                return cache[key]['value']

            # computing
            result = function(*args, **kw)

            # store the result
            cache[key] = {'value': result, 'time': time.time()}

            return result

        return __memoize

    return _memoize


@memoize()
def very_complex_shit(a, b):
    return a + b


@memoize(1)
def very_very_complex_shit(a, b, c):
    return a + b + c


print very_complex_shit(2, 4)
print very_complex_shit(2, 4)
print very_very_complex_shit(2, 1, 7)
