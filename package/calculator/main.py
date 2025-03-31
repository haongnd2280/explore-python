# main.py

from calculator import add, subtract


def main():
    a, b = 10, 5
    print(f"{a} + {b} = {add(a, b)}")
    print(f"{a} - {b} = {subtract(a, b)}")


if __name__ == "__main__":
    main()