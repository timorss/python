# create a a json
import json
from pathlib import Path
movies = [
    {
        "id": 1,
        "title": "terminatir",
        "year": 1989
    },
    {
        "id": 2,
        "title": "fast",
        "year": 1991
    }

]

data = json.dumps(movies)
print(data)
Path("movies.json").write_text(data)
