from datetime import datetime

from sqlalchemy import text

from config.database import database
from config.logger import logger

from models.repository import Repository

class PostgresLoader:

    def load_github_repositories(self,repositories: list[Repository]):


        query = text("""
        INSERT INTO staging.github_repositories (

            repository_id,
            name,
            full_name,
            owner_login,
            owner_type,
            description,
            language,
            stars,
            forks,
            watchers,
            open_issues,
            default_branch,
            is_private,
            repository_url,
            created_at,
            updated_at,
            pushed_at,
            raw_ingested_at

        )

        VALUES (

            :repository_id,
            :name,
            :full_name,
            :owner_login,
            :owner_type,
            :description,
            :language,
            :stars,
            :forks,
            :watchers,
            :open_issues,
            :default_branch,
            :is_private,
            :repository_url,
            :created_at,
            :updated_at,
            :pushed_at,
            :raw_ingested_at

        )

        ON CONFLICT (repository_id)

        DO UPDATE SET

            stars = EXCLUDED.stars,
            forks = EXCLUDED.forks,
            watchers = EXCLUDED.watchers,
            open_issues = EXCLUDED.open_issues,
            updated_at = EXCLUDED.updated_at,
            pushed_at = EXCLUDED.pushed_at,
            raw_ingested_at = EXCLUDED.raw_ingested_at;
        """)

        with database.engine.begin() as conn:

            for repo in repositories:

                conn.execute(
                    query,
                    {
                        "repository_id": repo.repository_id,
                        "name": repo.name,
                        "full_name": repo.full_name,
                        "owner_login": repo.owner_login,
                        "owner_type": repo.owner_type,
                        "description": repo.description,
                        "language": repo.language,
                        "stars": repo.stars,
                        "forks": repo.forks,
                        "watchers": repo.watchers,
                        "open_issues": repo.open_issues,
                        "default_branch": repo.default_branch,
                        "is_private": repo.is_private,
                        "repository_url": repo.repository_url,
                        "created_at": repo.created_at,
                        "updated_at": repo.updated_at,
                        "pushed_at": repo.pushed_at,
                        "raw_ingested_at": repo.raw_ingested_at,
                    },
                )

        logger.success(f"Loaded {len(repositories)} repositories into staging.")