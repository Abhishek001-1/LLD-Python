from dataclasses import dataclass
from datetime import datetime
from .log_level import Loglevel

@dataclass
class LogMessage:
    level: Loglevel
    message: str
    timestamp: datetime
     