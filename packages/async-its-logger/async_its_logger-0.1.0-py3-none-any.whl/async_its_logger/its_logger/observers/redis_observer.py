import yaml
import json
import asyncio
from its_logger.log_observer import LogObserver
import redis.asyncio as redis  # Import the asyncio client from redis-py

class RedisObserver(LogObserver):
    def __init__(self, config_path="config.yaml"):
        # Load configuration from YAML file
        with open(config_path, "r") as file:
            config = yaml.safe_load(file)

        self.redis_host = config["redis"]["host"]
        self.redis_port = config["redis"]["port"]
        self.redis_db = config["redis"]["db"]
        self.redis_list = config["redis"]["redis_list"]
        # Use provided execution_time_key or default to "execution_times"
        self.execution_time_key = config["redis"].get("execution_time_key", "execution_times")
        self.batch_size = config["logging"]["batch_size"]
        self.max_wait_time = config["logging"]["max_wait_time"]
        self.retry_delay = config["logging"]["retry_delay"]
        self.max_retries = config["logging"]["max_retries"]

        self.batch = []  # Buffer for batched log entries
        self.lock = asyncio.Lock()  # To protect access to the batch

    async def update(self, log_entry: dict):
        """Batch and push logs to Redis and store execution time if applicable."""
        async with self.lock:
            # Append the log entry as a JSON string to the batch
            self.batch.append(json.dumps(log_entry))
            print(f"[DEBUG] Appended log entry; current batch size: {len(self.batch)}")

            # If the log indicates a request completion, store the execution time
            if log_entry["status"] == "INFO" and "completed in" in log_entry["message"]:
                # Extract execution time from the message; adjust parsing if needed
                execution_time = log_entry["message"].split(" ")[-2]
                r = await redis.from_url(f"redis://{self.redis_host}:{self.redis_port}/{self.redis_db}")
                await r.hset(self.execution_time_key, log_entry["task_id"], execution_time)
                print(f"[DEBUG] Stored execution time for task {log_entry['task_id']}")
                await r.close()

            # If batch size is reached, flush the batch
            if len(self.batch) >= self.batch_size:
                await self.flush_batch()

    async def flush_batch(self):
        """Push the batched logs to Redis with retries and exponential backoff."""
        delay = self.retry_delay
        for attempt in range(self.max_retries):
            try:
                r = await redis.from_url(f"redis://{self.redis_host}:{self.redis_port}/{self.redis_db}")
                await r.rpush(self.redis_list, *self.batch)
                await r.close()
                print(f"[DEBUG] Flushed batch with {len(self.batch)} logs to Redis.")
                self.batch = []  # Clear the batch after successful push
                return
            except Exception as e:
                print(f"[ERROR] Redis batch push failed (Attempt {attempt+1}): {e}")
                await asyncio.sleep(delay)
                delay *= 2  # Exponential backoff
        print("[CRITICAL] Redis batch push failed after retries.")

    async def auto_flush(self):
        """Periodically flush logs if they have been waiting too long."""
        while True:
            await asyncio.sleep(self.max_wait_time)
            async with self.lock:
                if self.batch:
                    await self.flush_batch()

    def start_auto_flush(self, loop):
        """Schedule the auto_flush task on the provided running loop."""
        loop.create_task(self.auto_flush())
