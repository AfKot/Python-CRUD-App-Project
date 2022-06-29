from application import db
from application.models import Movies, Directors

db.drop_all()
db.create_all()

sample_directors = Directors(
    dir_name = "Sample Director"
)
db.session.add(sample_directors)
db.session.commit()

sample_movies = Movies(
    movie_name = "Sample Movie",
    rel_yr = 2012
)
db.session.add(sample_movies)
db.session.commit()