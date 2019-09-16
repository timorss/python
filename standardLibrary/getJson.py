import json
from pathlib import Path

data = Path("movies.json").read_text()  # string
movies = json.loads(data)
print(movies[0]['title'])
