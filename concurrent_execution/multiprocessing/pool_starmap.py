# Python3.8

import time 
import multiprocessing as mp 
from typing import Iterable

from demo import timer


def add_numbers(*args: Iterable[float]) -> float:
    time.sleep(2)
    return sum(args)

@timer
def main():
    n_cores = mp.cpu_count()
    print(f"Cores available: {n_cores}")

    values = (
        (1, 2, 3), 
        (3, 4), 
        (5, 6), 
        (7, 8, 10, 12)
    )

    with mp.Pool() as pool:
        results: Iterable[float] = pool.starmap(add_numbers, values)  
        print(f"Results: {results}")


if __name__ == "__main__":
    main()     
