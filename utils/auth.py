# -*- coding: utf-8 -*-
"""This module provides functions related to authentication.

The functions provided are most likely to be used with
`flask_jwt` to authenticate and identify a user.

"""

from utils.hash import verify_hash

from models.user import UserModel


def authenticate(username: str, password: str):
    """The function authenticates with username and password.

    Args:
        username (str): User's username
        password (str): User's password (before hashed)

    Returns:
        models.user.UserModel: If the user is found and the
        provided password is correct. Otherwise, `None` will
        be returned.

    """
    user = UserModel.find_by_username(username)
    if user and verify_hash(password, user.password_hash):
        return user


def identity(payload: dict):
    """The function identifies a user from JWT.

    Args:
        payload (dict): Should contain the `identity` key

    Returns:
        models.user.UserModel: If the user is found and the
        provided password is correct. Otherwise, `None` will
        be returned.

    """
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)
