# Python3.8 

import time
from typing import Tuple, List
import multiprocessing as mp 

from demo import timer


def convert_number_to_x(number: int) -> str:
    time.sleep(2)
    return number * "x"

@timer
def main():
    n_cores = mp.cpu_count()
    print(f"Cores available: {n_cores}")

    values: Tuple[int, ...] = tuple(range(1, n_cores + 1))      # increase the values to exceed the number of cores 
                                                                # -> time increases becase some values will have to wait for cores to be available

    # Use Pool.map to allocate each task to each available core
    with mp.Pool() as pool:
        results: List[str] = pool.map(convert_number_to_x, values)   # parallelize function executions over multiple input values
        print(f"Results: {results}")


if __name__ == "__main__":
    main()      # time ~ 2s because there are some overhead time for creating processes 
