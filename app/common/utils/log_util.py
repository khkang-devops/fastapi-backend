import logging
from logging.config import dictConfig
from app.config.config import APIConfig

# log_level
config = APIConfig()
log_level = config.log_level.upper()

# set log config
dictConfig(
    {
        "version": 1,
        "disable_existing_loggers": True,
        "formatters": {
            "default": {
                "format": "[%(asctime)s] [%(levelname)-8s] [%(filename)s:%(lineno)d] - %(message)s"
            }
        },
        "handlers": {
            "console": {
                "formatter": "default",
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stdout",
                "level": "DEBUG",
            }
        },
        "root": {"handlers": ["console"], "level": log_level},
        "loggers": {
            "gunicorn": {"propagate": True},
            "gunicorn.access": {"propagate": True},
            "gunicorn.error": {"propagate": True},
            "uvicorn": {"propagate": True},
            "uvicorn.access": {"propagate": True},
            "uvicorn.error": {"propagate": True},
        }
    }
)

# get logger
def get_logger(module_name=__name__):
    if module_name:
        logger = logging.getLogger(module_name)
        logger.debug(module_name)
    else:
        logger = logging.getLogger()

    logger.setLevel(log_level)

    return logger