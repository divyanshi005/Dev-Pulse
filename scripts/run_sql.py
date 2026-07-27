from pathlib import Path

from sqlalchemy import text

from config.database import database
from config.logger import logger

DDL_FOLDER = Path("warehouse/ddl")
VIEW_PATH = Path("warehouse/views")

def execute_sql_file(conn, sql_file):

    sql = sql_file.read_text().strip()

    if not sql:
        logger.warning(f"Skipping empty file: {sql_file.name}")
        return

    sql_without_comments = "\n".join(
        line
        for line in sql.splitlines()
        if not line.strip().startswith("--")
    ).strip()

    if not sql_without_comments:
        logger.warning(f"Skipping comment-only file: {sql_file.name}")
        return

    conn.execute(text(sql))

    logger.success(f"Finished {sql_file.name}")

def run_all_migrations():
    with database.engine.begin() as conn:

        logger.info("Running DDL...")

        for sql_file in sorted(DDL_FOLDER.glob("*.sql")):

            logger.info(f"Running {sql_file.name}")

            execute_sql_file(conn, sql_file)

        logger.info("Creating analytics views...")

        for sql_file in sorted(VIEW_PATH.glob("*.sql")):

            logger.info(f"Running {sql_file.name}")

            execute_sql_file(conn, sql_file)

if __name__ == "__main__":
    run_all_migrations()


'''
This version handles:

✅ Empty files
✅ Comment-only files
✅ Normal SQL files
'''