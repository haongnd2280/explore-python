def log_func_call(func): 
    """Log information about when each function is called 
    and with what arguments.
    """

    def wrapper(*args, **kwargs):
        print(f'Calling {func.__name__} with args: {args}, kwargs: {kwargs}.')
        
        return func(*args, **kwargs)     # Implement the function 
    
    return wrapper      # return the wrapper function itself, not the function call 

@log_func_call
def add(a, b): 
    return a + b

@log_func_call
def subtract(a, b):
    return a - b

# Whenever we call add or subtract, it will log information about the functin call. 
add(5, 3)
subtract(5, 3)