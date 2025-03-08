import yaml
import asyncio
from its_logger.log_observer import LogObserver
from datadog_api_client.v2 import ApiClient, Configuration
from datadog_api_client.v2.api.logs_api import LogsApi
import certifi  # Make sure to install certifi (pip install certifi)


class DatadogObserver(LogObserver):
    def __init__(self, config_path="config.yaml"):
        # Load configuration from YAML file
        with open(config_path, "r") as file:
            config = yaml.safe_load(file)
        self.api_key = config["datadog"]["api_key"]
        self.app_key = config["datadog"].get("app_key", None)
        # IMPORTANT: Set host to the base URL only (without /api/v2/logs)
        host = config["datadog"].get("endpoint", "https://http-intake.logs.datadoghq.com")

        # Configure the Datadog API client
        self.configuration = Configuration()
        self.configuration.host = host
        self.configuration.api_key["apiKeyAuth"] = self.api_key
        if self.app_key:
            self.configuration.api_key["appKeyAuth"] = self.app_key

        # Use certifi to set the CA certificate location so SSL verification passes
        self.configuration.ssl_ca_cert = certifi.where()

    async def update(self, log_entry: dict):
        """
        Submit the log entry to Datadog using the new Datadog API client.
        The call is wrapped with asyncio.to_thread to avoid blocking the async event loop.
        """

        def submit_log():
            with ApiClient(self.configuration) as api_client:
                logs_api = LogsApi(api_client)
                try:
                    # submit_log expects a list of log entries
                    response = logs_api.submit_log(body=[log_entry])
                    return response
                except Exception as e:
                    print(f"[ERROR] Datadog log submission failed: {e}")
                    return None

        response = await asyncio.to_thread(submit_log)
        if response is None:
            print("[ERROR] Datadog rejected log: no response received.")
