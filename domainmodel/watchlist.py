from domainmodel.movie import Movie
import random


class WatchList:
    def __init__(self):
        self.__watchList = []
        self.__genre_list = []

    def add_movie(self, movie):
        if movie not in self.__watchList:
            self.__watchList.append(movie)

    def remove_movie(self, movie):
        if movie in self.__watchList:
            self.__watchList.remove(movie)

    def select_movie_to_watch(self, index):
        if index >= len(self.__watchList):
            return None
        else:
            return self.__watchList[index]

    def size(self):
        return len(self.__watchList)

    def first_movie_in_watchlist(self):
        if len(self.__watchList) == 0:
            return None
        else:
            return self.__watchList[0]

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.__watchList) == 0:
            raise StopIteration
        else:
            return self.__watchList.pop(0)

    def choose_random(self):
        n = random.randint(0, len(self.__watchList))
        return self.__watchList[n-1]


watchlist = WatchList()
watchlist.add_movie(Movie("Moana", 2016))
watchlist.add_movie(Movie("Ice Age", 2002))
watchlist.add_movie(Movie("Guardians of the Galaxy", 2012))
print(watchlist.choose_random())