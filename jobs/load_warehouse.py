from loaders.warehouse_loader import WarehouseLoader
from config.logger import logger

loader = WarehouseLoader()

logger.info("Loading dimensions...")

loader.load_languages()
loader.load_owners()

loader.load_repositories()
loader.load_metrics()

loader.load_questions()
loader.load_tags()
loader.load_question_tags()
loader.load_question_metrics()

logger.success("Warehouse loading complete.")