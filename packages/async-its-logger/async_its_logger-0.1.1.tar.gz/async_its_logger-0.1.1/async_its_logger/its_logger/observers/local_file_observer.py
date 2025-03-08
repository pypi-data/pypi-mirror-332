import json
import os
import datetime
import yaml
from its_logger.log_observer import LogObserver

class LocalFileObserver(LogObserver):
    def __init__(self, config_path="config.yaml"):
        with open(config_path, "r") as file:
            config = yaml.safe_load(file)
        self.log_directory = config["logging"]["local_log_path"]
        os.makedirs(self.log_directory, exist_ok=True)
        print(f"[DEBUG] LocalFileObserver: Log directory set to {self.log_directory}")

    async def update(self, log_entry: dict):
        """Append log entry to a daily rotating log file."""
        filename = os.path.join(
            self.log_directory, f"log_{datetime.datetime.utcnow().date()}.log"
        )
        try:
            with open(filename, "a") as file:
                file.write(json.dumps(log_entry) + "\n")
            print(f"[DEBUG] LocalFileObserver: Wrote log entry to {filename}")
        except Exception as e:
            print(f"[ERROR] LocalFileObserver: Failed to write log entry: {e}")
