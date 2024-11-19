import logging 


logger = logging.getLogger(__name__)
logging.basicConfig(
    # filename="demo.log",
    # filemode="w",
    level=logging.DEBUG,
    # format="%(asctime)s:%(levelname)8s:%(name)10s:%(message)s",
    format="%(asctime)s::%(levelname)s::%(name)s::%(message)s",
    datefmt="%d/%m/%Y %H:%M:%S %p",
    encoding="utf-8"
)

logger.info("Hello World!")

# print(logger)