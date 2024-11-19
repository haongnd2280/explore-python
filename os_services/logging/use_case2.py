# Logging using multiple handlers and formatters

# Ví dụ: Đôi khi sẽ hữu ích nếu ứng dụng của ta log message của tất cả severity level vào một file text
# và đồng thời log các message có level >= error ra giao diện để tiện giám sát (monitor)
# => Cần định nghĩa một file handler và một console handler với cấu hình (log level) tương ứng và thêm nó vào logger object

import logging


logger = logging.getLogger("use_case2")
logger.setLevel(logging.DEBUG)

# Create file handler which logs even debug messages
file_handler = logging.FileHandler("use_case2.log")
file_handler.setLevel(logging.DEBUG)

# Create console handler with a higher log level
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.ERROR)

# Create formatter and add it to the handlers
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add the handlers to logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)


# Application code
logger.debug("Debug message")
logger.info("Info message")
logger.warning("Warning message")
logger.error("Error message")
logger.critical("Critical message")
