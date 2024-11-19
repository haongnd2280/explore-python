# Python3.8

import os 
from functools import wraps
from time import perf_counter
from datetime import datetime
import multiprocessing as mp


# Helper functions 
def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = perf_counter()
        result = func(*args, **kwargs)
        end_time = perf_counter()
        execution_time = end_time - start_time
        print(f"@{func.__name__}. Execution time: {execution_time:.5f} seconds")

        return result
    
    return wrapper

def timestamp() -> str:
    return f"{datetime.now():%H:%M:%S}"


# Main functions 
def main_func(verbose=False):
    if verbose:
        process_id = os.getpid()
        process_name = mp.current_process().name
        print(f"Starting {process_name}. PID: {process_id} {timestamp()}")

    for _ in range(10 ** 8):
        pass

    if verbose:
        print(f"{process_name} finished! {timestamp()}")

@timer
def mp_main():
    process1 = mp.Process(name="Process 1", target=main_func, args=(True,))
    process2 = mp.Process(name="Process 2", target=main_func, args=(True,))

    process1.start()
    process2.start()

    process1.join()
    process2.join()

@timer
def sequential_main():
    main_func()
    main_func()

if __name__ =="__main__":
    mp_main()
    sequential_main()      # The execution time is approximately 2x of multiprocess_main








