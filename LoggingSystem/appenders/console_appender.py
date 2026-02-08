from .base_appender import LogAppender

class ConsoleAppender(LogAppender):
    def append(self, message: str):
        print(message)