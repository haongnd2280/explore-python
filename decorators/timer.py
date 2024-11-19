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

        print(f'@timer. {func.__name__}. Execution time: {(end - start) * 1000} ms.')
        return result
    
    return wrapper

@timer
def fibonacci_list(n):
    """Compute the nth fibonacci number using list.
    """

    numbers = []     # a list to store all fibonacci numbers along the way
    a, b = 0, 1
    while len(numbers) < n:
        numbers.append(a)
        a, b = b, a + b

    return numbers[-1]


if __name__ == '__main__':
    result = fibonacci_list(100_000)
