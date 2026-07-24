import requests
from datetime import datetime, timedelta
from config.settings import settings
from config.logger import logger


class GitHubExtractor:
    """
    Handles all GitHub API interactions.
    """

    BASE_URL = "https://api.github.com"

    def __init__(self):
        self.headers = {
            "Authorization": f"Bearer {settings.GITHUB_TOKEN}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        }

    def get_trending_repositories(self,pages: int = 3,per_page: int = 10):

        url = f"{self.BASE_URL}/search/repositories"
        query = self.get_trending_query()
        all_repositories = []
        for page in range(1, pages + 1):
            params = {
            "q": query,
            "sort": "stars",
            "order": "desc",
            "per_page": per_page,
            "page": page
        }

       
            logger.info(f"Fetching page {page}...")

            response = requests.get(
                url,
                headers=self.headers,
                params=params,
                timeout=30,
            )

            response.raise_for_status()
            data = response.json()

            items = data["items"]
            if not items:
                break
            all_repositories.extend(items)

        logger.success(
                f"Fetched {len(all_repositories)} repositories."
            )
        return {"items": all_repositories}


    def get_trending_query(self, days: int = 30) -> str:
        """
        Build a GitHub search query for trending repositories.
        """

        since = (
            datetime.utcnow()
            - timedelta(days=days)
        ).strftime("%Y-%m-%d")
   
        return f"created:>{since}"


# NOTE: this extrator's job is only to fetch the files, not to save it. 
# to save it, we use github_ingestion.py 
# the extracor has no idea where the data is stored
# if later we want to use aws s3, azure blob storage, etc. we can do it without changing the extractor. 
# this is called loose coupling 
