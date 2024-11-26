# Đo lường dung lượng bộ nhớ được sử dụng bởi một hàm nào đó. 
# Hữu ích cho việc tối ưu performance, phát hiện memory leaks hoặc high memory usage trong một phần nào đó của code. 
# Hữu ích cho việc xử lý dữ liệu, xử lý ảnh, hoặc các phép toán xử lý dữ liệu lớn. 

import tracemalloc
from functools import wraps


def measure_memory(func):
    """This decorator prints the top memory-consuming lines of the function execution.
    Provides insight into potential memory bottlenecks in the function.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        start_snapshot = tracemalloc.take_snapshot()

        result = func(*args, **kwargs)

        end_snapshot = tracemalloc.take_snapshot()
        tracemalloc.stop()

        # Compare memory usage before and after the function call
        stats = end_snapshot.compare_to(start_snapshot, "lineno")

        print(f"Memory usage stats for function '{func.__name__}':")
        for stat in stats[:5]:  # Show top 5 memory-consuming lines
            print(stat)

        return result

    return wrapper


if __name__ == "__main__":
    @measure_memory
    def create_large_list(size):
        # Simulate memory-expensive operation
        return [x**2 for x in range(size)]         # this is the most memory-expensive operation
    

    # Execution
    create_large_list(1_000_000)
