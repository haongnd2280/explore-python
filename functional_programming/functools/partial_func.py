from functools import partial


def multiply(x, y): 
    """Original function. 
    """

    return x * y 


# Create a partial function with the first argument fixed to 2 
double = partial(multiply, 2) 

# Call the partial function with only one argument, e.g, the second argument 
result = double(5)    # this is equivalent to multiply(2, 5)
print(result) 


# ---- Define a decorator that mimics the partial function ----
def partial(*args, **kwargs):
    def decorator(func):

        def wrapper(*args_wrapper, **kwargs_wrapper):
            return func(*args, *args_wrapper, **kwargs, **kwargs_wrapper)
        return wrapper
        
    return decorator

@partial(2)
def multiply(x, y): 
    return x * y

result = multiply(5)
print(result)