import json
from its_logger.log_observer import LogObserver

class ConsoleObserver(LogObserver):
    async def update(self, log_entry: dict):
        """Print log entry to the console."""
        print(json.dumps(log_entry, indent=2))
