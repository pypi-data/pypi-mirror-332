import time
import yaml
from its_logger.async_its_logger import AsyncITSLogger
from its_logger.observers.mongodb_observer import MongoDBObserver
from its_logger.observers.redis_observer import RedisObserver
from its_logger.observers.datadog_observer import DatadogObserver
from its_logger.observers.s3_observer import S3Observer
from its_logger.observers.local_file_observer import LocalFileObserver
from its_logger.observers.console_observer import ConsoleObserver
import asyncio

# Load configuration
with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)

# Initialize logger (which creates its own event loop in a background thread)
logger = AsyncITSLogger()

# Register enabled observers dynamically
if config["logging"]["enable_datadog"]:
    print("Datadog observer enabled.")
    datadog_observer = DatadogObserver()
    logger.register_observer(datadog_observer)

if config["logging"]["enable_s3"]:
    print("S3 observer enabled.")
    s3_observer = S3Observer()
    logger.register_observer(s3_observer)

if config["logging"]["enable_local_file"]:
    print("Local file observer enabled.")
    local_file_observer = LocalFileObserver()
    logger.register_observer(local_file_observer)

if config["logging"]["enable_console"]:
    print("Console observer enabled.")
    console_observer = ConsoleObserver()
    logger.register_observer(console_observer)

if config["logging"]["enable_mongodb"]:
    print("Mongo observer enabled.")
    mongodb_observer = MongoDBObserver()
    logger.register_observer(mongodb_observer)
    # Start auto-flush for MongoDB observer using the logger's loop
    asyncio.run_coroutine_threadsafe(mongodb_observer.auto_flush(), logger.loop)

if config["logging"]["enable_redis"]:
    print("Redis observer enabled.")
    redis_observer = RedisObserver()
    logger.register_observer(redis_observer)
    #logger.loop.call_soon_threadsafe(redis_observer.start_auto_flush, logger.loop)
    asyncio.run_coroutine_threadsafe(redis_observer.auto_flush(), logger.loop)

# Example usage: simulate a request processing function
def process_request():
    task_id = logger.generate_task_id()
    print(f"Generated Task ID: {task_id}")

    start_time = time.time()
    logger.log("MyApp", "RequestHandler", task_id=task_id, message="Request started.")

    try:
        for i in range(3):
            logger.log("MyApp", f"ProcessingStep{i+1}", task_id=task_id, message=f"Processing step {i+1}...")
            time.sleep(1)  # Simulate processing time
        raise Exception("Something went wrong!")
    except Exception as e:
        logger.log(
            "MyApp",
            "ErrorHandler",
            task_id=task_id,
            status="ERROR",
            message="An error occurred while processing the request",
            exception=e
        )

    end_time = time.time()
    execution_time = round(end_time - start_time, 2)
    logger.log(
        "MyApp",
        "RequestHandler",
        task_id=task_id,
        status="INFO",
        message=f"Request completed in {execution_time} seconds."
    )

# Run simulated requests
for _ in range(1):
    process_request()
    time.sleep(2)

print("Main application finished.")
