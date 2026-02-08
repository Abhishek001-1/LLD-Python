from logger.logger import Logger
from logger.log_level import Loglevel
from appenders.console_appender import ConsoleAppender

logger = Logger(
    level = Loglevel.INFO,
    appender=ConsoleAppender()
)

logger.debug("This is a debug message")  # This will not be logged
logger.info("This is an info message")   # This will be logged
logger.warn("This is a warning message") # This will be logged
logger.error("This is an error message") # This will be logged