from pathlib import Path

from sqlalchemy import text

from config.database import database
from config.logger import logger

DDL_FOLDER = Path("warehouse/ddl")


def run_all_migrations():
    sql_files = sorted(DDL_FOLDER.glob("*.sql"))

    with database.engine.begin() as conn:
        for sql_file in sql_files:

            logger.info(f"Running {sql_file.name}")

            sql = sql_file.read_text().strip()

            # Skip empty files
            if not sql:
                logger.warning(f"Skipping empty file: {sql_file.name}")
                continue

            # Skip files that only contain SQL comments
            sql_without_comments = "\n".join(
                line for line in sql.splitlines()
                if not line.strip().startswith("--")
            ).strip()

            if not sql_without_comments:
                logger.warning(f"Skipping comment-only file: {sql_file.name}")
                continue

            conn.execute(text(sql))

            logger.success(f"Finished {sql_file.name}")


if __name__ == "__main__":
    run_all_migrations()


'''
This version handles:

✅ Empty files
✅ Comment-only files
✅ Normal SQL files
'''