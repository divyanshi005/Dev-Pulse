from sqlalchemy import text

from config.database import database
from config.logger import logger


class WarehouseLoader:

    def load_languages(self):
        """
        Load unique programming languages into dim_language.
        """

        sql = """
        INSERT INTO warehouse.dim_language (language_name)

        SELECT DISTINCT language

        FROM staging.github_repositories

        WHERE language IS NOT NULL

        ON CONFLICT (language_name)

        DO NOTHING;
        """

        with database.engine.begin() as conn:
            result = conn.execute(text(sql))

        logger.success(f"Inserted {result.rowcount} languages.")

    def load_owners(self):
        """
        Load unique repository owners into dim_owner.
        """

        sql = """
        INSERT INTO warehouse.dim_owner (owner_login, owner_type)

        SELECT DISTINCT owner_login, owner_type

        FROM staging.github_repositories

        WHERE owner_login IS NOT NULL

        ON CONFLICT (owner_login)

        DO NOTHING;
        """

        with database.engine.begin() as conn:
            result = conn.execute(text(sql))

        logger.success(f"Inserted {result.rowcount} owners.")

    def load_repositories(self):
        """
        Load repositories into dim_repository.
        """

        sql = """
        INSERT INTO warehouse.dim_repository (repository_id, owner_id, language_id, name, full_name, description, default_branch, repository_url, created_at)

        SELECT r.repository_id, o.owner_id, l.language_id, r.name, r.full_name, r.description, r.default_branch, r.repository_url, r.created_at

        FROM staging.github_repositories r

        INNER JOIN warehouse.dim_owner o ON r.owner_login = o.owner_login

        LEFT JOIN warehouse.dim_language l ON r.language = l.language_name

        WHERE r.repository_id IS NOT NULL

        ON CONFLICT (repository_id)

        DO UPDATE SET
        description=EXCLUDED.description,
        default_branch=EXCLUDED.default_branch,
        last_loaded=CURRENT_TIMESTAMP;
        """

        with database.engine.begin() as conn:
            result = conn.execute(text(sql))

        logger.success(f"Inserted {result.rowcount} repositories.")


    def load_metrics(self):

        """

Load repository metrics into fact_repository_metrics.

        """



        sql = """

        INSERT INTO warehouse.fact_repository_metrics (repository_id, stars, forks, watchers, open_issues, updated_at, pushed_at)



        SELECT repository_id, stars, forks, watchers, open_issues, updated_at, pushed_at



        FROM staging.github_repositories


        WHERE repository_id IS NOT NULL



        """



        with database.engine.begin() as conn:

            result = conn.execute(text(sql))



        logger.success(f"Inserted {result.rowcount} repository metrics.")
