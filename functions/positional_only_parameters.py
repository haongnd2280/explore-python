from typing import Any


def foo(a: Any, b: Any, /, c: Any, d: Any) -> None: 
    """Tất cả tham số đứng trước ký tự / đều là positional-only parameters.
    Ở ví dụ này, a, b đứng trước ký tự / => chúng là positional-only parameters.
    """

    print(a, b, c, d, sep=", ")


if __name__ == "__main__":
    foo(1, 2, 3, 4)            # valid call
    foo(1, 2, c=3, d=4)        # valid call
    foo(a=1, b=2, c=3, d=4)    # invalid call, raise TypeError
