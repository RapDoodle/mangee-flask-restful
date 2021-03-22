# -*- coding: utf-8 -*-
"""The module provides functions related to startup routines."""

from utils.constants import CONFIG_PATH
from flask import Flask
from json import loads
import os


def create_app(name: str, config: dict) -> Flask:
    """Creates a flask object based on configurations.

    Note:
        This function does not start the server. It only 
        creates a Flask object.

    Args:
        name (str): The name of the application, in the most
            cases, please use __name__. For more information,
            please vist:
            https://flask.palletsprojects.com/en/1.1.x/api/#flask.Flask
        config (dict): A dictionary containing configurations.

    Returns:
        flask.app.Flask: The configured flask application.

    """
    app = Flask(name)
    for key in config.keys():
        app.config[key] = config[key]
    return app


def load_config(name: str) -> dict:
    """Reads configuration and retusn as a dict.

    Args:
        name (str): The name of the configuration. By default, 
        it should be stored in `/config` and should be a 
        json file.

    Example:
        By default, using ``load_config(name='dev')``, the 
        function reads the configuration in
        ``./configurations/dev.json``. To change the directory 
        to store the configurations, please change `CONFIG_PATH`.

    Returns:
        dict: The file in the form of python dictionary.
    
    """
    return loads(open(os.path.join(CONFIG_PATH, name+'.json'), 'r').read())
