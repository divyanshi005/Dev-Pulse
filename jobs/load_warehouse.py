from loaders.warehouse_loader import WarehouseLoader
from config.logger import logger

loader = WarehouseLoader()

logger.info("Loading dimensions...")

loader.load_languages()
loader.load_owners()
loader.load_repositories()

logger.info("Loading facts...")

loader.load_metrics()

logger.success("Warehouse loading complete.")