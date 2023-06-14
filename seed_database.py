"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system('dropdb ratings')
os.system('createdb ratings')

model.connect_to_db(server.app)
model.db.create_all()

with open('data/movies.json') as f:
    movie_data = json.loads(f.read())

def create_app():
    app = Flask(__name__)
    app.config.from_object("project.config")

    import project.models

    with app.app_context():
        db.create_all()

    return app


movies_in_db = []
for Movie in movie_data:
    title, overview, poster_path = (
        Movie["title"],
        Movie["overview"],
        Movie["poster_path"],
    )
    release_date = datetime.strptime(Movie["release_date"], "%Y-%m-%d")

    db_movie = crud.create_movie(title, overview, release_date, poster_path)
    movies_in_db.append(db_movie)

for n in range(10):
    email = f"user{n}@test.com"  
    password = "test"

    user = crud.create_user(email, password)
    model.db.session.add(user)

    for _ in range(10):
        random_movie = choice(movies_in_db)
        score = randint(1, 5)

        rating = crud.create_rating(user, random_movie, score)
        model.db.session.add(rating)

model.db.session.commit()

model.db.session.add_all(movies_in_db)
model.db.session.commit()