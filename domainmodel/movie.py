from domainmodel.genre import Genre
from domainmodel.actor import Actor
from domainmodel.director import Director


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
        if type(d) == Director:
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