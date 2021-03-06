from flask_jwt import JWT
from utils.auth.auth import authenticate, identity

jwt = JWT(authentication_handler=authenticate, identity_handler=identity)

def init_jwt(app):
    app.config['JWT_AUTH_URL_RULE'] = '/api/auth'   
    jwt.init_app(app)
    

