"""Initialize Flask app."""

import os

from flask import Flask

import cs235flix.adapters.repository as repo
from cs235flix.adapters.memory_repository import MemoryRepository, populate


def create_app(test_config=None):
    """Construct the core application."""

    # Create the Flask app object.
    app = Flask(__name__)

    # Configure the app from configuration-file settings.
    app.config.from_object('config.Config')
    data_path = os.path.join('cs235flix', 'datafiles')

    if test_config is not None:
        # Load test configuration, and override any configuration settings.
        app.config.from_mapping(test_config)
        data_path = app.config['TEST_DATA_PATH']

    # Create the MemoryRepository implementation for a memory-based repository.
    repo.repo_instance = MemoryRepository()
    populate(data_path, repo.repo_instance)

    with app.app_context():
        # Register blueprints.
        from cs235flix.home import home
        app.register_blueprint(home.home_blueprint)

        from cs235flix.movies import movies
        app.register_blueprint(movies.movies_blueprint)

        from cs235flix.authentication import authentication
        app.register_blueprint(authentication.authentication_blueprint)

        from cs235flix.utilities import utilities
        app.register_blueprint(utilities.utilities_blueprint)

    return app