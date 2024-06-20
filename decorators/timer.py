import time
from functools import wraps


def timer(func):
    """Decorator to automate the measurement of execution time.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()

        print(f'@Timer: {func.__name__}. Execution time: {(end - start) * 1000} ms.')
        return result
    
    return wrapper