import logging


logging.warning("%s before you %s", "Look", "leap!")

a = "Hello"
b = "World"
logging.warning("%s after you %s", a, b)

a, b = 1, 2
logging.warning("%s after you %s", a, b)
logging.warning(f"{a} after you {b}")        # f-string is more readable
