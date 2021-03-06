from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_sqlalchemy import SQLAlchemy
from flask_jwt import jwt_required
from models.user import UserModel
from resources.user_register import UserRegister
from utils.http_server.simple_server import server
from core.jwt import init_jwt
import os

# ================================================================
# Setting up flask

app = Flask(__name__)
app.secret_key = 'ergU*YrerwrHWR*(UyHOGkH))'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

# ================================================================
# Setting up flask-JWT
init_jwt(app)

# Set up the path for registeration
api.add_resource(UserRegister, '/api/register')

@app.before_first_request
def create_tables():
	db.create_all()

# ================================================================
# Simple HTTP Server. Should be able to be disabled
app.register_blueprint(server)
# ================================================================

# Spin up the server
if __name__ == '__main__':
	from core.db import db
	db.init_app(app)
	app.run(host='0.0.0.0', port=80, debug=True)
