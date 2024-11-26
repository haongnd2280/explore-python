# Ký tự * đóng vai trò làm một marker: đánh dấu rằng các tham số sau ký tự này đều là keyword-only parameters.

def create_user(name: str, *, is_admin: bool) -> None:
    print(f"name: {name}, is_admin: {is_admin}")

def calculate_total(
    price: float, 
    *, 
    discount: float = 0, 
    tax: float = 0.1
) -> float:
    """This helps prevent ambiguity and avoid unintentional errors 
    caused by passing arguments in the wrong order.
    """

    total = price * (1 - discount) * (1 + tax)    # điều này giúp tránh pass nhầm giá trị của discout và tax nếu pass theo positional argument
    return total

# Advance example: Combining *args (variable-length positional arguments) with keyword-only arguments
def display_values(*args, sep: str, end: str):   # như này thì sep và end sẽ tự động là keyword-only arguments.
    """Displays values with a custom separator and end.
    """

    print(*args, sep=sep, end=end)


if __name__ == "__main__":
    create_user("haongnd", is_admin=True)
    # create_user("admin", True)    # TypeError

    calculate_total(100, discount=0.2, tax=0.15)   

    display_values(1, 2, 3, sep=" | ", end="\n")
    