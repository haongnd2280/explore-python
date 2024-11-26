import time
from functools import wraps


def cache_with_expiry(duration):
    """A caching decorator to cache the result of each function call
    with a specific expiration time (seconds).
    """

    def decorator(func):
        cache = {}

        @wraps(func)
        def wrapper(*args, **kwargs):
            # TODO: Elaborate to ensure kwargs are in the same order
            key = (args, frozenset(kwargs.items()))        # list all the parameters; use frosenzet to ensure key is hashable (immutable)
            if key in cache:
                result, timestamp = cache[key]
                if time.time() - timestamp < duration:      # Check if the result is within the duration
                    return result
            
            print(f"Call function with arguments: {key}.")
            result = func(*args, **kwargs)
            cache[key] = (result, time.time())

            return result
        
        return wrapper

    return decorator


if __name__=="__main__":
    @cache_with_expiry(duration=5)   # cache result for 5 seconds
    def fibonacci(n):
        if n <= 1:
            return n
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)
    
    print(fibonacci(10))    # Output: 55
    print(fibonacci(10))    # Output: 55 (cached result, no recomputation)
    time.sleep(6)
    print(fibonacci(10))    # Output: 55 (cached result expired, recomputation)
        
