import yaml
import datetime
import pymongo
import asyncio
from its_logger.log_observer import LogObserver

class MongoDBObserver(LogObserver):
    def __init__(self, config_path="config.yaml"):
        with open(config_path, "r") as file:
            config = yaml.safe_load(file)

        self.mongo_uri = config["mongodb"]["uri"]
        self.database_name = config["mongodb"]["database"]
        self.collection_name = config["mongodb"]["collection"]
        self.execution_collection = config["mongodb"]["execution_times_collection"]
        self.batch_size = config["logging"]["batch_size"]
        self.max_wait_time = config["logging"]["max_wait_time"]
        self.retry_delay = config["logging"]["retry_delay"]
        self.max_retries = config["logging"]["max_retries"]

        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.database_name]
        self.collection = self.db[self.collection_name]
        self.execution_db = self.db[self.execution_collection]

        self.batch = []
        self.lock = asyncio.Lock()


    async def update(self, log_entry: dict):
        """Batch insert logs into MongoDB."""
        async with self.lock:
            log_entry["timestamp"] = datetime.datetime.utcnow()
            self.batch.append(log_entry)

            # If it's a request completion log, store execution time
            if log_entry["status"] == "INFO" and "completed in" in log_entry["message"]:
                execution_time = log_entry["message"].split(" ")[-2]  # Extract execution time
                self.execution_db.update_one(
                    {"task_id": log_entry["task_id"]},
                    {"$set": {"execution_time": execution_time, "timestamp": datetime.datetime.utcnow()}},
                    upsert=True
                )

            if len(self.batch) >= self.batch_size:
                await self.flush_batch()

    async def flush_batch(self):
        """Insert batch of logs into MongoDB with retries."""
        max_retries = self.max_retries
        delay = self.retry_delay

        for attempt in range(max_retries):
            try:
                self.collection.insert_many(self.batch)
                self.batch = []  # Clear batch after insert
                return
            except pymongo.errors.PyMongoError as e:
                print(f"[ERROR] MongoDB batch insert failed (Attempt {attempt+1}): {e}")
                await asyncio.sleep(delay)
                delay *= 2  # Exponential backoff
        print("[CRITICAL] MongoDB insert failed after retries.")

    async def auto_flush(self):
        """Flush logs periodically if waiting too long."""
        while True:
            await asyncio.sleep(self.max_wait_time)
            async with self.lock:
                if self.batch:
                    await self.flush_batch()

    def start_auto_flush(self, loop):
        """Start the auto-flush background task on the provided loop."""
        loop.create_task(self.auto_flush())