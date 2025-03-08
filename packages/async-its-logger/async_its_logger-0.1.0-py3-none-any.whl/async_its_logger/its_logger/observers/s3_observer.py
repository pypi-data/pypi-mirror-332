import json
import datetime
import yaml
import boto3
import asyncio
from botocore.exceptions import NoCredentialsError, BotoCoreError
from its_logger.log_observer import LogObserver

class S3Observer(LogObserver):
    def __init__(self, config_path="config.yaml"):
        with open(config_path, "r") as file:
            config = yaml.safe_load(file)

        self.s3_bucket = config["aws"]["s3_bucket_name"]
        self.s3_prefix = config["aws"]["s3_prefix"]
        self.batch_size = config["logging"]["batch_size"]
        self.max_wait_time = config["logging"]["max_wait_time"]
        self.retry_delay = config["logging"]["retry_delay"]
        self.max_retries = config["logging"]["max_retries"]

        self.s3_client = boto3.client("s3")
        self.batch = []
        self.lock = asyncio.Lock()

        # Start auto-flush background task
        asyncio.create_task(self.auto_flush())

    async def update(self, log_entry: dict):
        """Batch logs before sending them to S3."""
        async with self.lock:
            self.batch.append(log_entry)

            if len(self.batch) >= self.batch_size:
                await self.flush_batch()

    async def flush_batch(self):
        """Upload batched logs to S3 with retries."""
        filename = f"{self.s3_prefix}/batch_{datetime.datetime.utcnow().isoformat()}.json"
        max_retries = self.max_retries
        delay = self.retry_delay

        for attempt in range(max_retries):
            try:
                self.s3_client.put_object(
                    Bucket=self.s3_bucket, Key=filename, Body=json.dumps(self.batch)
                )
                self.batch = []  # Clear batch after upload
                return
            except (NoCredentialsError, BotoCoreError) as e:
                print(f"[ERROR] S3 batch upload failed (Attempt {attempt+1}): {e}")
                await asyncio.sleep(delay)
                delay *= 2  # Exponential backoff
        print("[CRITICAL] S3 batch upload failed after retries.")

    async def auto_flush(self):
        """Flush logs periodically if waiting too long."""
        while True:
            await asyncio.sleep(self.max_wait_time)
            async with self.lock:
                if self.batch:
                    await self.flush_batch()
