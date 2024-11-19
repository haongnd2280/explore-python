# Configure logging from a file (.conf file)

import logging
import logging.config


logging.config.fileConfig("logging.conf")

logger = logging.getLogger("file_config")   # this is error-prone 
# logger = logging.getLogger()                # get the root logger

# Application code
logger.debug("debug message")
logger.info("info message")
logger.warning("warn message")
logger.error("error message")
logger.critical("critical message")