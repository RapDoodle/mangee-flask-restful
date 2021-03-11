# -*- coding: utf-8 -*-
"""This module provides provides a simple HTTP(S) server.

Note:
    It is not recommended to serve the frontend in this manner
    for the sake of performance. According to Flask's official
    documentation, it is of best practice to activate your
    webserver's `X-Sendfile` support.
        
    For more information, visit:
    https://flask.palletsprojects.com/en/1.1.x/api/#flask.send_from_directory

Example:
    In app.py, add:
        from utils.http_server.simple_server import server
        app.register_blueprint(server)

"""

from flask import Blueprint, send_from_directory

server = Blueprint('http_server', __name__)


@server.route('/<path:folder>/<path:file>', methods=['GET'])
def send_static_file(folder, file):
    print(folder, file)
    return send_from_directory(f'web/{folder}', file)


@server.route('/', defaults={'path': ''})
@server.route('/<path:path>', methods=['GET'])
def index(path):
    return send_from_directory(directory='web', filename='index.html')


@server.errorhandler(404)
def resource_not_found(e):
    return index(path='')
