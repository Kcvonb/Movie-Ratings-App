from model import db, User, Movie, Rating, connect_to_db

if __name__ == '__main__':
    from server import app
    connect_to_db(app)

def create_user(email, password):

    user = User(email=email, password=password)

    return user

def create_movie(title, overview, release_date, poster_path):
    
    Movie = Movie(        
        title=title,
        overview=overview,
        release_date=release_date,
        poster_path=poster_path,
    )
    
    return Movie

def create_rating(user, movie, score):

    rating = Rating(user=user, movie=movie, score=score)

    return rating



def get_movies():
    """Return all movies."""

    return Movie.query.all()






user1 = User.query.get(1)
movie1 = Movie.query.get(1)

rating = create_rating(User.query.get(1), movie1, 5)


# movie1 = create_movie("Title Name", "")

