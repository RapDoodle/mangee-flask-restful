# -*- coding: utf-8 -*-
from flask_restful import Api
from logging import Formatter, FileHandler
import logging
import sys

# Core modules
from core.jwt import init_jwt
from core.db import init_db, db
from core.lang import init_lang
from core.startup import create_app, load_config

# User defined resources
from resources.user_register import UserRegister
from resources.demo import Demo


if __name__ == '__main__':
    # Get the app according to the provided profile
    app = create_app(name=__name__, config=load_config(sys.argv[1]))

    # Setup logger
    file_handler = FileHandler('app.log')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(
        Formatter('%(asctime)s %(levelname)s: %(message)s'))
    app.logger.addHandler(file_handler)

    # Initialize RESTful service
    api = Api(app)

    # Set up the path for registeration
    api.add_resource(UserRegister, '/api/register')
    api.add_resource(Demo, '/api/demo')

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

    # Initialize the launguage system.
    init_lang(app)
    
    # Spin up the server
    app.run(host=app.config.get('HOST', '127.0.0.1'), 
        port=app.config.get('PORT', 5000))
