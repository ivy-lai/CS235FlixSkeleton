from datetime import datetime
from domainmodel.movie import Movie


class Review:

    def __init__(self, movie, review_text, rating):
        if type(rating) == int and 1 <= rating <= 10:
            self.__rating = rating
        else:
            self.__rating = None
        self.__datetime = datetime.date(datetime.now())
        self.__movie = movie
        self.__review_text = review_text

    @property
    def movie(self):
        return self.__movie

    @property
    def review_text(self):
        return self.__review_text

    @property
    def rating(self):
        return self.__rating

    def __repr__(self):
        return f"<Review for {self.__movie}: {self.__rating}, {self.__review_text}>"

    def __eq__(self, other):
        if isinstance(other, Review):
            return (self.__movie, self.__review_text, self.__rating, self.__datetime) == (other.__movie, other.__review_text, other.__rating, other.__datetime)
        else:
            return False


class Movie:
    def __init__(self, title: str, year: int):
        if title != "" and type(title) == str:
            self.__title = title.strip()
        else:
            self.__title = None

        if year >= 1900:
            self.__year = year
        else:
            self.__year = None

        self.__description = None
        self.__actorList = []
        self.__genreList = []
        self.__runtime = None
        self.__director_full_name = None

    @property
    def movie(self):
        return self.__title, self.__year, self.__description, self.__actorList, self.__genreList, self.__runtime, self.__director_full_name

    def __repr__(self):
        return f"<Movie {self.__title}, {self.__year}>"

    def __eq__(self, other):
        if isinstance(other, type(self)):
            return (self.__title == other.__title) and (self.__year == other.__year)
        else:
            return False

    def __lt__(self, other):
        return (self.__title, self.__year) < (other.__title, other.__year)

    def __hash__(self):
        return hash((self.__title, str(self.__year)))

    def add_actor(self, a):
        if type(a) == Actor:
            self.__actorList.append(a)

    def remove_actor(self, a):
        if a in self.__actorList:
            self.__actorList.remove(a)

    def add_genre(self, g):
        if type(g) == Genre:
            self.__genreList.append(g)

    def remove_genre(self, g):
        if g in self.__genreList:
            self.__genreList.remove(g)

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        if type(title) == str:
            self.__title = title

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, desc):
        if type(desc) == str:
            self.__description = desc.strip()

    @property
    def director(self):
        return self.__director_full_name

    @director.setter
    def director(self, d):
        if type(d) != list:
            self.__director_full_name = d

    @property
    def actors(self):
        return self.__actorList

    @actors.setter
    def actors(self, a):
        if type(a) == list:
            self.__actorList = a

    @property
    def genres(self):
        return self.__genreList

    @genres.setter
    def genres(self, genre):
        if type(genre) == list:
            self.__genreList = genre

    @property
    def runtime_minutes(self):
        return self.__runtime

    @runtime_minutes.setter
    def runtime_minutes(self, time):
        if type(time) == int and time >= 1:
            self.__runtime = time
        else:
            raise ValueError


class Actor:
    def __init__(self, actor_full_name: str):
        if actor_full_name == "" or type(actor_full_name) is not str:
            self.__actor_full_name = None
        else:
            self.__actor_full_name = actor_full_name.strip()
        self.__colleagueList = []

    @property
    def actor_full_name(self) -> str:
        return self.__actor_full_name

    def __repr__(self):
        return f"<Actor {self.__actor_full_name}>"

    def __eq__(self, other):
        if isinstance(other, Actor):
            return self.__actor_full_name == other.__actor_full_name
        else:
            return False

    def __lt__(self, other):
        return self.__actor_full_name < other.__actor_full_name

    def __hash__(self):
        return hash(self.__actor_full_name)

    def add_actor_colleague(self, colleague):
        self.__colleagueList.add(colleague)

    def check_if_this_actor_worked_with(self, colleague):
        if colleague in self.__colleagueList:
            return True
        else:
            return False


class Genre:
    def __init__(self, genre_name: str):
        if genre_name == "" or type(genre_name) is not str:
            self.__genre_name = None
        else:
            self.__genre_name = genre_name.strip()

    @property
    def genre_name(self) -> str:
        return self.__genre_name

    def __repr__(self):
        return f"<Genre {self.__genre_name}>"

    def __eq__(self, other):
        if isinstance(other, Genre):
            return self.__genre_name == other.__genre_name
        else:
            return False

    def __lt__(self, other):
        return self.__genre_name < other.__genre_name

    def __hash__(self):
        return hash(self.__genre_name)


class Director:

    def __init__(self, director_full_name: str):
        if director_full_name == "" or type(director_full_name) is not str:
            self.__director_full_name = None
        else:
            self.__director_full_name = director_full_name.strip()

    @property
    def director_full_name(self) -> str:
        return self.__director_full_name

    def __repr__(self):
        return f"<Director {self.__director_full_name}>"

    def __eq__(self, other):
        if isinstance(other, Director):
            return self.__director_full_name == other.__director_full_name
        else:
            return False

    def __lt__(self, other):
        return self.__director_full_name < other.__director_full_name

    def __hash__(self):
        return hash(self.__director_full_name)
