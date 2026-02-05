from backend.app.services.sync_service import SyncService
from backend.app.utils import logger
from typing import Dict, Any

class SyncController:
    def __init__(self):
        self.sync_service = SyncService()

    def initiate_sync(self, data: Dict[str, Any]) -> None:
        """
        Initiate the data synchronization process.

        :param data: The data to be synchronized.
        """
        try:
            logger.info("Initiating synchronization process.")
            self.sync_service.synchronize_data(data)
        except Exception as e:
            logger.error("Error initiating sync: {}", e)