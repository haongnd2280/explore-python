# Use case 3: Logging to multiple destinations
# Ví dụ: Ta muốn log đến console và file với format khác nhau và ở các hoàn cảnh khác nhau.
# Giả sử ta muốn log message có level >= DEBUG vào file, và level >= INFO vào console.
# Giả sử rằng log file có chứa timestamp còn console thì không cần.

import logging

# Set up logging to file
logger = logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(name)-15s %(levelname)-8s %(message)s",
    datefmt="%d/%m/%Y %H:%M:%S",
    filename="use_case3.log",
    filemode="w"
)
# Define a handler which write INFO messages or higher to the sys.stderrư
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Create a formatter which is simpler for console use
formatter = logging.Formatter("%(name)-15s: %(levelname)-8s %(message)s")
console_handler.setFormatter(formatter)
logging.getLogger("").addHandler(console_handler)   # add the console handler to the root logger

# Now, we can log to the root logger or any other logger
# First the root...
logging.info("Info message from root logger.")

# Now, define a couple of other loggers which might reperesent areas in your application
logger1 = logging.getLogger("use_case3.area1")
logger2 = logging.getLogger("use_case3.area2")

logger1.debug("Debug message from logger1.")
logger1.info("Info message from logger1.")
logger2.warning("Warning message from logger2.")
logger2.error("Error message from logger2.")