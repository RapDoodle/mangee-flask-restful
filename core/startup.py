# -*- coding: utf-8 -*-
"""The module provides functions related to startup routines."""

import os
import re
import logging
from datetime import timedelta
from utils.constants import CONFIG_PATH
from flask import Flask
from json import loads
from core.jwt import init_jwt
from core.db import init_db, db
from core.lang import init_lang


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
        if key.startswith('@'):
            # Parser of special configuration
            value = config[key]
            if isinstance(value, dict):
                # Cases where direct parsing is not possible
                func_type = value['type']
                if func_type == 'timedelta':
                    assert isinstance(value['args'], dict)
                    value = timedelta(**value['args'])
            elif isinstance(value, str):
                # Reference with '@'
                value = re.sub('@(RESTFUL_PREFIX)::*', \
                    config['RESTFUL_PREFIX'], config[key])
            # Remove the prefix '@' before storing into the config
            app.config[key[1:]] = value
            continue
        app.config[key] = config[key]
    return app


def init_core_modules(app):
    """Initializes the core modules for the given context.

    It initializes the following plugins/functions in order:
        1). Launguage system
        2). Logger
        3). Flask-JWT-Extended
        4). Flask-SQLAlchemy
        5). HTTP server (testing only)
    
    Args:
        app (flask.app.Flask): A Flask application

    """
    # Initialize the launguage system.
    init_lang(app)

    # Setup logger
    file_handler = logging.FileHandler('app.log')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(
        logging.Formatter('%(asctime)s %(levelname)s: %(message)s'))
    app.logger.addHandler(file_handler)

    # Setting up flask-JWT
    init_jwt(app)

    # Setup database
    init_db(app)
    with app.app_context():
        db.create_all()

    # Simple HTTP server. Not recommended in production.
    if (app.config.get('ENABLE_SIMPLE_HTTP_SERVER', False)):
        from utils.http_server import server
        app.register_blueprint(server)


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


def run(app):
    """Spins up a Flask application.
    
    Args:
        app (flask.app.Flask): A Flask application

    """
    app.run(host=app.config.get('HOST', '127.0.0.1'), 
        port=app.config.get('PORT', 5000))