# -*- coding: utf-8 -*-
import sys

# Flask modules
from flask_restful import Api

# Core modules
from core.startup import create_app, load_config, init_core_modules, run

# User defined resources
from resources.user_register import UserRegister
from resources.demo import Demo


if __name__ == '__main__':
    # Get the app according to the provided profile
    app = create_app(name=__name__, config=load_config(sys.argv[1]))

    # Initialize core modules
    init_core_modules(app)

    # Initialize RESTful service
    api = Api(app)

    # Set up the path RESTful services
    api.add_resource(UserRegister, app.config['RESTFUL_PREFIX']+'/register')
    api.add_resource(Demo, app.config['RESTFUL_PREFIX']+'/demo')
    
    # Spin up the server
    run(app)
