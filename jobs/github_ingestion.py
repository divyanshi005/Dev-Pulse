from extractors.github_extractor import GitHubExtractor
from transformers.github_transformer import GitHubTransformer
from loaders.postgres_loader import PostgresLoader
from utils.json_writer import JSONWriter

extractor = GitHubExtractor()
transformer = GitHubTransformer()
loader = PostgresLoader()

data = extractor.get_trending_repositories()

JSONWriter.save(data, "github")

repositories = transformer.transform(data)

loader.load_github_repositories(repositories)

print(f"Loaded {len(repositories)} repositories")