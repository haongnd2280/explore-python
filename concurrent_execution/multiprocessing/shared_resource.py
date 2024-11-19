import multiprocessing as mp 


numbers: list[int] = [0]

def func():
    global numbers

    numbers.extend([1, 2, 3])
    print(f"Process data: {numbers}")

def main():
    process = mp.Process(target=func)
    process.start()
    process.join()

    print(f"Main data: {numbers}")


if __name__ == "__main__":
    main()



