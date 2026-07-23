from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine

from config.settings import settings
from config.logger import logger


class Database:
    def __init__(self):
        database_url = (
            f"postgresql+psycopg2://"
            f"{settings.DB_USER}:{settings.DB_PASSWORD}"
            f"@{settings.DB_HOST}:{settings.DB_PORT}"
            f"/{settings.DB_NAME}"
            f"?sslmode={settings.DB_SSLMODE}"
        )

        self.engine: Engine = create_engine(
            database_url,
            pool_pre_ping=True,
            future=True,
        )

    def test_connection(self):
        try:
            with self.engine.connect() as conn:
                result = conn.execute(text("SELECT version();"))
                version = result.scalar_one()

                logger.success("Connected to PostgreSQL!")
                logger.info(version)

                return True

        except Exception as e:
            logger.exception(e)
            return False


database = Database()