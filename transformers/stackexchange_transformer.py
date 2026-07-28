from datetime import datetime
from models.question import Question
class StackExchangeTransformer:

    @staticmethod
    def transform(raw_data):
        """
        Transform raw Stack Exchange JSON into Question objects.
        """
        questions=[]
        for item in raw_data["items"]:
            question = Question(
                question_id=item["question_id"],
                title=item["title"],
                owner_name=item.get("owner", {}).get("display_name"),
                score=item["score"],
                answer_count=item["answer_count"],
                view_count=item["view_count"],
                creation_date=datetime.fromtimestamp(item["creation_date"]),
                tags=item["tags"]
            )
            questions.append(question)
        return questions