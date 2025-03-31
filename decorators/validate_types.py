# Tạo một decorator để đảm bảo rằng input parameters của hàm phải thỏa mãn tiêu chí hay ràng buộc nào đó. 
# Điều này giúp đảm bảo data integrity (toàn vẹn dữ liệu), ngăn ngừa lỗi và xử lý edge cases một cách khéo léo. 

from functools import wraps


def validate_types(*expected_types):
    """A simple validation decorator to ensure that a function's arguments
    are of the correct types.
    """
    
    def decorator(func):
        @wraps(func)

        def wrapper(*args, **kwargs):
            # Execute type check
            # Only check the type of the positional arguments passed
            for arg, expected_type in zip(args, expected_types):
                if not isinstance(arg, expected_type):
                    raise TypeError(f"Argument {arg} is not of type {expected_type}. Passed in type: {type(arg)}.")
            
            # Type check done, all things good, invoke the main function
            return func(*args, **kwargs)
        
        return wrapper
    
    return decorator


if __name__=="__main__":
    @validate_types(int, int)          # This returns the decorator function
    def add_numbers(a, b):             # This returns the wrapper function
        return a + b
    
    result = add_numbers(5, 10)         # OK
    result = add_numbers(5.0, 10.0)     # Error: wrong type
