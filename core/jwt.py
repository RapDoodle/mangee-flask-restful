# -*- coding: utf-8 -*-
"""This core module handles the initialization of JWT."""

from flask_jwt_extended import JWTManager

from utils.auth import authenticate
from utils.auth import identity

jwt = JWTManager()


def init_jwt(app):
    """The function initializes `jwt` with the provided context.

    Args:
        app (flask.app.Flask): A Flask application

    """    
    jwt.init_app(app)
