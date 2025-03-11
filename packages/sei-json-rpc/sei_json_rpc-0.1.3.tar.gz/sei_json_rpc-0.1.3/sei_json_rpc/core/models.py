from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional, Any


@dataclass
class RPCResult:
    url: str
    method: str
    result: Any
    timestamp: datetime = datetime.now()

    def to_dict(self):
        return {
            "url": self.url,
            "method": self.method,
            "result": self.result,
            "timestamp": self.timestamp.isoformat()
        }
