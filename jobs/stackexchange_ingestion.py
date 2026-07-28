from extractors.stackexchange_extractor import StackExchangeExtractor,  StackExchangeExtractor
from transformers.stackexchange_transformer import StackExchangeTransformer
from loaders.postgres_loader import PostgresLoader
from utils.json_writer import JSONWriter

extractor = StackExchangeExtractor()
transformer = StackExchangeTransformer()
loader = PostgresLoader()

data = extractor.get_top_questions()

JSONWriter.save(data, "stackexchange")

questions = transformer.transform(data)

loader.load_stackexchange_questions(questions)

print(f"Loaded {len(questions)} questions")