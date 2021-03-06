# -*- coding: utf-8 -*-
"""This core module provides an instance of SQLAlchemy.

Example:
    In app.py, add:
        from utils.http_server.simple_server import server
        app.register_blueprint(server)

"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_db(app):
    """The function initializes `db` with the provided context.

    Args:
        app (flask.app.Flask): A Flask application

    """
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_AUTH_URL_RULE'] = '/api/auth'

    db.init_app(app)
