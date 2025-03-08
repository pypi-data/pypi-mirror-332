import asyncio
import json
import uuid
import yaml
import threading
import datetime
import socket
import traceback
from its_logger.log_observer import LogObserver

class AsyncITSLogger:
    _instance = None  # Singleton instance

    def __new__(cls, config_path="config.yaml"):
        if not cls._instance:
            cls._instance = super(AsyncITSLogger, cls).__new__(cls)
        return cls._instance

    def __init__(self, config_path="config.yaml"):
        if not hasattr(self, "initialized"):  # Ensure init runs only once
            self.load_config(config_path)
            self.log_queue = asyncio.Queue()
            self.instance_id = self.get_instance_id()
            self.observers = []  # List of observers
            self.loop = asyncio.new_event_loop()
            self.thread = threading.Thread(target=self._start_loop, daemon=True)
            self.thread.start()

            # Start the batch processor
            asyncio.run_coroutine_threadsafe(self.batch_log_sender(), self.loop)

            self.initialized = True

    def _start_loop(self):
        """Run the asyncio loop in a separate thread."""
        asyncio.set_event_loop(self.loop)
        self.loop.run_forever()

    def load_config(self, path):
        with open(path, "r") as file:
            config = yaml.safe_load(file)
        self.config = config
        self.batch_interval = config["logging"]["batch_interval"]

    def get_instance_id(self):
        try:
            return socket.gethostname()
        except Exception:
            return "unknown-instance"

    @staticmethod
    def generate_task_id():
        """Generate a unique task ID (UUID)."""
        return str(uuid.uuid4())

    def register_observer(self, observer: LogObserver):
        """Register a new observer."""
        self.observers.append(observer)

    async def notify_observers(self, log_entry):
        """Notify all observers asynchronously."""
        tasks = [observer.update(log_entry) for observer in self.observers]
        await asyncio.gather(*tasks)

    def log(self, application_name, agent_name, task_id=None, status="INFO", message="", exception=None):
        """Log a message (fire-and-forget)."""
        # Capture traceback if an exception is provided
        error_trace = traceback.format_exc() if exception else None

        log_entry = {
            "uuid": str(uuid.uuid4()),
            "application_name": application_name,
            "agent_name": agent_name,
            "task_id": task_id or self.generate_task_id(),
            "instance_id": self.instance_id,
            "status": status,
            "timestamp": datetime.datetime.utcnow().isoformat(),
            "message": message,
            "traceback": error_trace  # Store traceback if available
        }
        asyncio.run_coroutine_threadsafe(self.log_queue.put(log_entry), self.loop)

    async def batch_log_sender(self):
        """Process logs continuously."""
        while True:
            # Process all available logs immediately
            while not self.log_queue.empty():
                log_entry = await self.log_queue.get()
                print(f"[DEBUG] Logger: Notifying observers with log entry: {log_entry}")
                await self.notify_observers(log_entry)

            # Wait for the next batch interval
            await asyncio.sleep(self.batch_interval)
