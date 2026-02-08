from .base_appender import LogAppender

class FileAppender(LogAppender):
    def __init__(self, file_path: str):
        self.file_path = file_path
    
    def append(self, message: str):
        with open(self.file_path, "a") as file:
            file.write(message + "\n")