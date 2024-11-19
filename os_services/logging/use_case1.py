# Use case 1: Using logging in multiple modules (scripts)

import logging
import auxiliary_module


# Create logger with 'spam_application'
logger = logging.getLogger("spam_app")
logger.setLevel(logging.DEBUG)

# Create file handler which logs even debug messages
file_handler = logging.FileHandler("spam.log")
file_handler.setLevel(logging.DEBUG)

# Create console handler with a higher log level
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.ERROR)

# Create formatter and add it to the handlers
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add the handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)


# Start to write log messages 
logger.info("Create an instance of auxiliary_module.Auxiliary")
a = auxiliary_module.Auxiliary()
logger.info("Done creating an instance of auxiliary_module.Auxiliary")

logger.info("Calling auxiliary_module.Auxiliary.do_something")
a.do_something()
logger.info("Finished auxiliary_module.Auxiliary.do_something")

logger.info("Calling auxiliary_module.some_function()")
auxiliary_module.some_function()
logger.info("Done with auxiliary_module.some_function()")

logger.error("This error is logged to both file and console.")