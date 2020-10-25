from cs235flix.domainmodel.full_model import Movie
from cs235flix.domainmodel.full_model import Review


class User:
    def __init__(self, username, password):
        if type(username) == str:
            self.__username = username.strip().lower()
        else:
            self.__username = None

        if type(password) == str:
            self.__password = password
        else:
            self.__password = None

        self.__watched_movies = []
        self.__reviews = []
        self.__time_spent_watching_movies_minutes = 0

    def __repr__(self):
        return f"<User {self.__username}>"

    def __eq__(self, other):
        if isinstance(other, type(self)):
            return self.__username == other.__username
        else:
            return False

    def __lt__(self, other):
        return self.__username < other.__user_name

    def __hash__(self):
        return hash((self.__username, self.__password))

    def watch_movie(self, movie):
        self.__watched_movies.append(movie)
        self.__time_spent_watching_movies_minutes += int(movie.runtime_minutes)

    def add_review(self, review):
        self.__reviews.append(review)

    @property
    def username(self):
        return self.__username

    @property
    def password(self):
        return self.__password

    @property
    def watched_movies(self):
        return self.__watched_movies

    @property
    def reviews(self):
        return self.__reviews

    @property
    def time_spent_watching_movies_minutes(self):
        return self.__time_spent_watching_movies_minutes
