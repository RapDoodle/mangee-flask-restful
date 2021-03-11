# -*- coding: utf-8 -*-
"""This core module handles the initialization of JWT."""

from flask_jwt import JWT
from utils.auth import authenticate, identity

jwt = JWT(authentication_handler=authenticate, identity_handler=identity)


def init_jwt(app):
    """The function initializes `jwt` with the provided context.

    Args:
        app (flask.app.Flask): A Flask application

    """
    app.config['JWT_AUTH_URL_RULE'] = '/api/auth'
    jwt.init_app(app)
