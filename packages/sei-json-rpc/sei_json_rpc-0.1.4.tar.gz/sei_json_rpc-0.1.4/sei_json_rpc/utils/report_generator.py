import csv
from datetime import datetime
from typing import List

from core.models import RPCResult


class ReportGenerator:
    @staticmethod
    def save_to_csv(results: List[RPCResult]):
        with open("report.csv", "a") as f:
            writer = csv.DictWriter(f, fieldnames=["timestamp", "url", "method", "result"])
            for res in results:
                writer.writerow({
                    "timestamp": datetime.now(),
                    "url": res.url,
                    "method": res.method,
                    "result": str(res.result)
                })
