import abc

class LogObserver(abc.ABC):
    """Abstract base class for log observers."""
    @abc.abstractmethod
    async def update(self, log_entry: dict):
        pass
