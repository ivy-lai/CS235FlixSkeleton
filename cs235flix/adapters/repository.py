import abc
from typing import List

from cs235flix.domainmodel.full_model import Movie, Actor, Director, Genre, Review, User, WatchList


repo_instance = None


class RepositoryException(Exception):

    def __init__(self, message=None):
        pass


class AbstractRepository(abc.ABC):

    @abc.abstractmethod
    def add_movie(self, movie: Movie):
        """ Adds an Movie to the repository. """
        raise NotImplementedError

    @abc.abstractmethod
    def add_director(self, director):
        """ Adds an Movie to the repository. """
        raise NotImplementedError

    @abc.abstractmethod
    def get_movie(self, title: str, year: int) -> Movie:
        """ Returns Movie with movie from the repository.

        If there is no Movie with the given movie, this method returns None.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_movie_by_id(self, movie_id: int) -> Movie:
        """ Returns Movie with movie from the repository.

        If there is no Movie with the given movie, this method returns None.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_movies_by_id(self, id_list) -> Movie:
        """ Returns Movie with movie from the repository.

        If there is no Movie with the given movie, this method returns None.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_genres(self):
        """ Returns Movie with movie from the repository.

        If there is no Movie with the given movie, this method returns None.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def add_genre(self, genre_name):
        """ Returns a list of Articles, whose ids match those in id_list, from the repository.

        If there are no matches, this method returns an empty list.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_directors(self):
        """ Returns Movie with movie from the repository.

        If there is no Movie with the given movie, this method returns None.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_actors(self):
        """ Returns Movie with movie from the repository.

        If there is no Movie with the given movie, this method returns None.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def add_actor(self, actor_name):
        """ Returns a list of Articles, whose ids match those in id_list, from the repository.

        If there are no matches, this method returns an empty list.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_movie_for_genre(self, id_list):
        """ Returns a list of Articles, whose ids match those in id_list, from the repository.

        If there are no matches, this method returns an empty list.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_movie_id_by_genre(self, genre_name: str):
        """ Returns a list of Articles, whose ids match those in id_list, from the repository.

        If there are no matches, this method returns an empty list.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_all_movies(self):
        """ Returns a list of Articles, whose ids match those in id_list, from the repository.

        If there are no matches, this method returns an empty list.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_number_of_movies(self):
        """ Returns a list of Articles, whose ids match those in id_list, from the repository.

        If there are no matches, this method returns an empty list.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def add_user(self, user):
        """ Returns a list of Articles, whose ids match those in id_list, from the repository.

        If there are no matches, this method returns an empty list.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_user(self, username):
        """ Returns a list of Articles, whose ids match those in id_list, from the repository.

        If there are no matches, this method returns an empty list.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def add_review(self, review):
        """ Returns a list of Articles, whose ids match those in id_list, from the repository.

        If there are no matches, this method returns an empty list.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_reviews(self):
        """ Returns a list of Articles, whose ids match those in id_list, from the repository.

        If there are no matches, this method returns an empty list.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_ratings(self):
        """ Returns a list of Articles, whose ids match those in id_list, from the repository.

        If there are no matches, this method returns an empty list.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_ids(self):
        """ Returns a list of Articles, whose ids match those in id_list, from the repository.

        If there are no matches, this method returns an empty list.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_movie_for_actor(self, actor):
        """ Returns a list of Articles, whose ids match those in id_list, from the repository.

                If there are no matches, this method returns an empty list.
                """
        raise NotImplementedError

    @abc.abstractmethod
    def get_movie_by_director(self, director):
        """ Returns a list of Articles, whose ids match those in id_list, from the repository.

                If there are no matches, this method returns an empty list.
                """
        raise NotImplementedError

    @abc.abstractmethod
    def get_watchlist(self):
        """ Returns a list of Articles, whose ids match those in id_list, from the repository.

                If there are no matches, this method returns an empty list.
                """
        raise NotImplementedError

    @abc.abstractmethod
    def add_watchlist(self, movie):
        """ Returns a list of Articles, whose ids match those in id_list, from the repository.

                If there are no matches, this method returns an empty list.
                """
        raise NotImplementedError

    @abc.abstractmethod
    def remove_watchlist(self, movie):
        """ Returns a list of Articles, whose ids match those in id_list, from the repository.

                If there are no matches, this method returns an empty list.
                """
        raise NotImplementedError