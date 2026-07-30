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

        sql1 = """
            INSERT INTO warehouse.dim_owner
            (
                owner_name,
                owner_type,
                platform
            )

            SELECT DISTINCT
                owner_login,
                owner_type,
                'github'

            FROM staging.github_repositories

            WHERE owner_login IS NOT NULL

            ON CONFLICT (owner_name, platform)
            DO NOTHING;
        """

        sql2="""
            INSERT INTO warehouse.dim_owner
            (
                owner_name,
                owner_type,
                platform
            )

            SELECT DISTINCT
                owner_name,
                NULL,
                'stackexchange'

            FROM staging.stackexchange_questions

            WHERE owner_name IS NOT NULL

            ON CONFLICT (owner_name, platform)
            DO NOTHING;
        """

        with database.engine.begin() as conn:
            github_result = conn.execute(text(sql1))
            stack_result = conn.execute(text(sql2))

        logger.success(
                f"Inserted "
                f"{github_result.rowcount + stack_result.rowcount} owners."
            )
    def load_repositories(self):
        """
        Load repositories into dim_repository.
        """

        sql = """
        INSERT INTO warehouse.dim_repository (repository_id, owner_id, language_id, name, full_name, description, default_branch, repository_url, created_at)

        SELECT r.repository_id, o.owner_id, l.language_id, r.name, r.full_name, r.description, r.default_branch, r.repository_url, r.created_at

        FROM staging.github_repositories r

        INNER JOIN warehouse.dim_owner o ON r.owner_login = o.owner_name AND o.platform = 'github'

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

        ON CONFLICT (repository_id)
        DO UPDATE SET
            stars = EXCLUDED.stars,
            forks = EXCLUDED.forks,
            watchers = EXCLUDED.watchers,
            open_issues = EXCLUDED.open_issues,
            updated_at = EXCLUDED.updated_at,
            pushed_at = EXCLUDED.pushed_at,
            collected_at = CURRENT_TIMESTAMP;



        """



        with database.engine.begin() as conn:

            result = conn.execute(text(sql))



        logger.success(f"Inserted {result.rowcount} repository metrics.")


    def load_questions(self):
            """
            Load questions into dim_question.
            """
    
            sql = """
            INSERT INTO warehouse.dim_question (question_id, title, owner_id, creation_date)
    
            SELECT r.question_id, r.title, o.owner_id, r.creation_date
    
            FROM staging.stackexchange_questions r
    
            INNER JOIN warehouse.dim_owner o ON r.owner_name = o.owner_name AND o.platform = 'stackexchange'
    
            WHERE r.question_id IS NOT NULL
    
            ON CONFLICT (question_id)
    
            DO UPDATE SET
            title=EXCLUDED.title,
            owner_id = EXCLUDED.owner_id,
            creation_date = EXCLUDED.creation_date;
            """
    
            with database.engine.begin() as conn:
                result = conn.execute(text(sql))
    
            logger.success(f"Inserted {result.rowcount} questions.")
    
    def load_tags(self):
        """
        Load tags into dim_tag.
        """

        sql = """
        INSERT INTO warehouse.dim_tag (tag_name)

        SELECT DISTINCT UNNEST(tags) AS tag_name

        FROM staging.stackexchange_questions

        WHERE tags IS NOT NULL

        ON CONFLICT (tag_name)

        DO NOTHING;
        """

        with database.engine.begin() as conn:
            result = conn.execute(text(sql))

        logger.success(f"Inserted {result.rowcount} tags.")

    def load_question_tags(self):
        """
        Load question-tag relationships into bridge_question_tag.
        """

        sql = """
        INSERT INTO warehouse.bridge_question_tag (question_id, tag_id)

        SELECT q.question_id, t.tag_id

        FROM staging.stackexchange_questions r

        INNER JOIN warehouse.dim_question q ON r.question_id = q.question_id

        CROSS JOIN LATERAL UNNEST(r.tags) AS u(tag_name)

        INNER JOIN warehouse.dim_tag t ON u.tag_name = t.tag_name

        WHERE r.question_id IS NOT NULL AND r.tags IS NOT NULL

        ON CONFLICT (question_id, tag_id)

        DO NOTHING;
        """

        with database.engine.begin() as conn:
            result = conn.execute(text(sql))

        logger.success(f"Inserted {result.rowcount} question-tag relationships.")

    def load_question_metrics(self):
        """
        Load question metrics into fact_question_metrics.
        """

        sql = """
        INSERT INTO warehouse.fact_question_metrics
        (
            question_id,
            score,
            answer_count,
            view_count
        )

        SELECT
            r.question_id,
            r.score,
            r.answer_count,
            r.view_count

        FROM staging.stackexchange_questions r

        INNER JOIN warehouse.dim_question q
            ON r.question_id = q.question_id

        ON CONFLICT (question_id)
        DO UPDATE SET
            score = EXCLUDED.score,
            answer_count = EXCLUDED.answer_count,
            view_count = EXCLUDED.view_count,
            last_loaded = CURRENT_TIMESTAMP;
        """

        with database.engine.begin() as conn:
            result = conn.execute(text(sql))

        logger.success(f"Inserted {result.rowcount} question metrics.")