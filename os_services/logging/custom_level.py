import logging
import logging.config 


config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {
            "format": "%(levelname)-8s - %(message)s"
        }
    },
    "filters": {
        "warnings_and_below": {
            "()": "__main__.filter_maker",        # the filter function
            "level": "WARNING"                    # the argument to the filter function
        }
    },
    "handlers": {
        "stdout": {
            "class": "logging.StreamHandler",
            "level": "INFO",
            "formatter": "simple",
            "stream": "ext://sys.stdout",
            "filters": ["warnings_and_below"]     # add filter for stdout handler
        },
        "stderr": {
            "class": "logging.StreamHandler",
            "level": "ERROR",
            "formatter": "simple",
            "stream": "ext://sys.stderr",
        },
        "file": {
            "class": "logging.FileHandler",
            "formatter": "simple",                # no level specified for file => use default level of root logger
            "filename": "app.log",
            "mode": "w"
        }
    },
    "root": {
        "level": "DEBUG",
        "handlers": [
            "stdout",
            "stderr",
            "file"  
        ]
    }
}

def filter_maker(level: str):
    level: int = getattr(logging, level)    # convert logging level to integer

    def filter(record): 
        return record.levelno <= level    
    
    return filter

# Start logging
logging.config.dictConfig(config)           # use dictConfig to read config JSON specified above
logging.debug("Debug message")
logging.info("Info message")
logging.warning("Warning message")
logging.error("Error message")
logging.critical("Critical message")

