import requests

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

    def get_trending_repositories(self):

        url = f"{self.BASE_URL}/search/repositories"

        params = {
            "q": "stars:>1000",
            "sort": "stars",
            "order": "desc",
            "per_page": 10,
        }

        logger.info("Fetching repositories from GitHub...")

        response = requests.get(
            url,
            headers=self.headers,
            params=params,
            timeout=30,
        )

        response.raise_for_status()

        logger.success("GitHub API request successful.")

        return response.json()


# NOTE: this extrator's job is only to fetch the files, not to save it. 
# to save it, we use github_ingestion.py 
# the extracor has no idea where the data is stored
# if later we want to use aws s3, azure blob storage, etc. we can do it without changing the extractor. 
# this is called loose coupling 
