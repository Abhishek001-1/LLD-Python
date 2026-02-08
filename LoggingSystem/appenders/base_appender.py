from abc import ABC, abstractmethod

class LogAppender(ABC):
    @abstractmethod
    def append(self, message: str):
        pass