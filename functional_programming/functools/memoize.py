# Memoization: aka caching

import inspect 
from functools import lru_cache


@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    
    return fib(n - 1) + fib(n - 2)

result = [fib(n) for n in range(16)]

print(fib.cache_info())
print(fib.cache_parameters())

# Clear cache result 
fib.cache_clear()
print(fib.cache_info())

print(fib.__wrapped__)    # return the wrapped (undecorated) function
result = fib.__wrapped__(20)
print(result)
print(fib.cache_info())


# ---- Example 2: Work well 
from functools import lru_cache

@lru_cache(maxsize=128)
def compute(x):
    print("Computing...", end=" ")
    return x * 2

# Call the decorated function with caching
print(compute(2))     # Output: "Computing..." then 4
print(compute(2))     # Output: 4 (cached result, no "Computing...")
print(compute.cache_info())

# Access the original function through __wrapped__ and call it without using the cache
print(compute.__wrapped__(2))   # Output: "Computing..." then 4
print(compute.cache_info()) 

# Rewrap the original function with a new cache size 
compute = lru_cache(maxsize=5)(compute.__wrapped__)
print(compute.cache_info())

print(inspect.getsource(lru_cache))
