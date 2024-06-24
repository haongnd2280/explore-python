"""Caching: kỹ thuật được sử dụng để lưu trữ kết quả của một lời gọi hàm rất tốn kém (tài nguyên, thời gian)
và sử dụng lại các kết quả đó khi gặp lại input đầu vào khi gọi hàm đó - nhờ đó mà ta không phải tính toán lại kết quả
=> tăng performance của chương trình. 
Cache: bộ nhớ đệm, bộ nhớ tạm. 
"""

from functools import wraps


def memoize(func):
    cache = {}          # This will initialize when you first define the function to pass to the decorator, 
                        # and remains when you call the function again and again with different arguments. 
    @wraps(func)
    def wrapper(*args):
        if args not in cache:        # for the fibonacci example, the args is the nth fibonacci number to be calculated 
            cache[args] = func(*args)
            print(f"{args} is not calculated yet.")
        else: 
            print(f"{args} is already cached.")

        return cache[args]
    
    return wrapper 

@memoize 
def fibonacci(n): 
    """Calculate fibonacci number by recursion - from bottom to top. 

    With the help of cached decorator, the calculation is real fast if we want to calculate multiple fibonacci numbers. 
    """

    if n <= 1: 
        return n 
    
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    print(fibonacci(10))   # This call will calculate fibonacci(10) and cache the result 
    print('-' * 50)
    print(fibonacci(15))   # This call will simultaneously calculate fibonacci(15) and reuse the cached result for fibonacci(10) and cache the new result
    print('-' * 50)
    print(fibonacci(10))   # This call will reuse the cached result for fibonacci(10) 
    print('-' * 50)



