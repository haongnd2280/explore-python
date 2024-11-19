# Logging to a file

import logging


logger = logging.getLogger(__name__)    # create a logger instane and call its methods
logging.basicConfig(
    filename="example.log",
    filemode="w",    # default is append
    encoding="utf-8",
    level=logging.DEBUG,
)

logger.debug("This message should go to the log file.")
logger.info("So should this.")
logger.warning("And this, too.")
logger.error("And non-ASCII stuff, too, like Tên tôi là.")

