from pathlib import Path
from datetime import datetime
import json

from config.logger import logger


class JSONWriter:

    @staticmethod
    def save(data, source: str):

        timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")

        folder = Path(f"data/raw/{source}")

        folder.mkdir(parents=True, exist_ok=True)

        filename = folder / f"{timestamp}.json"

        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        logger.success(f"Saved raw data to {filename}")

        return filename