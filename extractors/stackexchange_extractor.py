import requests

from config.logger import logger


class StackExchangeExtractor:
    """
    Handles all Stack Exchange API interactions.
    """

    BASE_URL = "https://api.stackexchange.com/2.3"

    def get_top_questions(self, pages=2, page_size=25):
        """
        Fetch top Stack Overflow questions.
        """
        url = f"{self.BASE_URL}/questions"

        params = {
            "site": "stackoverflow",
            "sort": "votes",
            "order": "desc",
            "pagesize": page_size,
        }
        all_questions = []
        for page in range(1, pages + 1):

            params["page"] = page

            logger.info(f"Fetching page {page}...")

            response = requests.get(
                url,
                params=params,
                timeout=30
            )

            response.raise_for_status()

            data = response.json()

            items = data["items"]

            if not items:
                break

            all_questions.extend(items)
        logger.success(f"Fetched {len(all_questions)} questions.")

        return {
            "items": all_questions
        }