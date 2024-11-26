# Partial function: hàm được tạo ra từ một hàm khác bằng cách cố định trước một vài tham số (đặt giá trị trước cho các tham số đó), 
# từ đó khi gọi hàm partial thì chỉ cần truyền giá trị cho các tham số còn lại.
# Use case: hữu ích khi ta có một hàm thường xuyên được gọi với tập các đối số giống nhau. 

from functools import partial


# Example in docs
base_two = partial(int, base=2)     # truyền trước đối số base=2 vào hàm int
base_two.__doc__ = "Convert base 2 string to an int."
print(base_two("10010"))
print(int("10010", base=2))         # kết quả giống với base_two


# Example 2 
def multiple(x, y, z):
    return x * y * z

partial_func = partial(multiple, 2)         # fix the first argument to 2; x=2
print(partial_func(3, 4))                   # Output: 24

partial_func = partial(multiple, 2, 3)      # x=2, y=3
print(partial_func(4))             

partial_func = partial(multiple, x=2, y=3)
print(partial_func(z=4))                    # cần chỉ rõ kwarg z=4, nếu không nó sẽ coi x=2 vì ta chưa chỉ rõ arg nào => lỗi vì x được gọi 2 lần (x=2, x=4) 


# Hảm functools.partial tương đương với hàm sau
def partial(func, /, *args, **kwargs):
    """An implementation of partial function that mimics functools.partial.
    """

    def wrapper(*fargs, **fkwargs):
        new_kwargs = {**kwargs, **fkwargs}
        result = func(*args, *fargs, **new_kwargs)   # args are passed before fwargs because they are preset
        return result
    
    # Set (read-only) attributes for the wrapper function
    wrapper.func = func
    wrapper.args = args
    wrapper.keywords = kwargs

    return wrapper

func = partial(multiple, 2)
# Print function attributes
print(func.func)
print(func.args)
print(func.keywords)

print(func(3, 4))             # 24

# Không thể (và không nên) sử dụng functools.partial như một decorator
