from datetime import datetime

from models.repository import Repository


class GitHubTransformer:

    @staticmethod
    def transform(data: dict) -> list[Repository]:

        repositories = []

        for repo in data["items"]:

            repositories.append(

                Repository(

                    repository_id=repo["id"],

                    name=repo["name"],

                    full_name=repo["full_name"],

                    owner_login=repo["owner"]["login"],

                    owner_type=repo["owner"]["type"],

                    description=repo["description"],

                    language=repo["language"],

                    stars=repo["stargazers_count"],

                    forks=repo["forks_count"],

                    watchers=repo["watchers_count"],

                    open_issues=repo["open_issues_count"],

                    default_branch=repo["default_branch"],

                    is_private=repo["private"],

                    repository_url=repo["html_url"],

                    created_at=datetime.fromisoformat(
                        repo["created_at"].replace("Z", "+00:00")
                    ),

                    updated_at=datetime.fromisoformat(
                        repo["updated_at"].replace("Z", "+00:00")
                    ),

                    pushed_at=datetime.fromisoformat(
                        repo["pushed_at"].replace("Z", "+00:00")
                    ),

                    raw_ingested_at=datetime.utcnow(),
                )

            )

        return repositories

        