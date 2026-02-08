from .log_message import LogMessage

class Formatter:
    def format(self, log_message: LogMessage):
        return f"[{log_message.timestamp}] {log_message.level.name}: {log_message.message}"