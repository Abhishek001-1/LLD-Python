from datetime import datetime
from .log_level import Loglevel
from .log_message import LogMessage
from .formatter import Formatter
from appenders.base_appender import LogAppender

class Logger:
    def __init__(self, level: Loglevel, appender: LogAppender):
        self.level = level
        self.appender = appender
        self.formatter = Formatter()

    def log(self, level: Loglevel, message: str):
        if level.value >= self.level.value:
            log_message = LogMessage(
                level = level,
                message = message,
                timestamp = datetime.now()
            )
            formatted = self.formatter.format(log_message)
            self.appender.append(formatted)
        
    def debug(self, message: str):
        self.log(Loglevel.DEBUG, message)
    
    def info(self, message: str):
        self.log(Loglevel.INFO, message)

    def warn(self, message: str):
        self.log(Loglevel.WARN, message)

    def error(self, message: str):
        self.log(Loglevel.ERROR, message)