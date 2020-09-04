from domainmodel.movie import Movie
from domainmodel.review import Review


class User:
    def __init__(self, user_name, password):
        if type(user_name) == str:
            self.__user_name = user_name.strip().lower()
        else:
            self.user_name = None

        if type(password) == str:
            self.__password = password
        else:
            self.__password = None

        self.__watched_movies = []
        self.__reviews = []
        self.__time_spent_watching_movies_minutes = 0

    def __repr__(self):
        return f"<User {self.__user_name}>"

    def __eq__(self, other):
        if isinstance(other, type(self)):
            return self.__user_name == other.__user_name
        else:
            return False

    def __lt__(self, other):
        return self.__user_name < other.__user_name

    def __hash__(self):
        return hash((self.__user_name, self.__password))

    def watch_movie(self, movie):
        self.__watched_movies.append(movie)
        self.__time_spent_watching_movies_minutes += int(movie.runtime_minutes)

    def add_review(self, review):
        self.__reviews.append(review)

    @property
    def user_name(self):
        return self.__user_name

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
