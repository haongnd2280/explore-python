import logging


# Create child loggers of "spam_app"
module_logger = logging.getLogger("spam_app.auxiliary")

class Auxiliary:
    def __init__(self):
        self.logger = logging.getLogger("spam_app.auxiliary.Auxiliary")
        self.logger.info("Create an instance of Auxiliary")

    def do_something(self):
        self.logger.info("Do something")
        a = 1 + 1
        self.logger.info("Done doing something")

def some_function():
    module_logger.info("Received a call to 'some_function'")

# module_logger.propagate = False
# module_logger.info("This won't be sent to the parent handler.")
