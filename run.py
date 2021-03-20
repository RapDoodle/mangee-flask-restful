from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from resources.user_register import UserRegister
from resources.demo import Demo
from core.jwt import init_jwt
from core.db import init_db, db
from core.lang import init_lang
from logging import Formatter, FileHandler

from core.startup import create_app, load_config

import logging
import sys
import os

# Spin up the server
if __name__ == '__main__':
    app = create_app(name=__name__, config=load_config(sys.argv[1]))
    file_handler = FileHandler('app.log')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(
        Formatter('%(asctime)s %(levelname)s: %(message)s'))
    
    app.logger.addHandler(file_handler)

    api = Api(app)

    # Setting up flask-JWT
    init_jwt(app)

    # Set up the path for registeration
    api.add_resource(UserRegister, '/api/register')
    api.add_resource(Demo, '/api/demo')

    @app.before_first_request
    def create_tables():
        db.create_all()

    # Simple HTTP server. Not recommended in production.
    if (app.config.get('ENABLE_SIMPLE_HTTP_SERVER', False)):
        from utils.http_server import server
        app.register_blueprint(server)

    init_db(app)
    init_lang(app)
    
    app.run(host=app.config.get('HOST', '127.0.0.1'), 
        port=app.config.get('PORT', 5000))
