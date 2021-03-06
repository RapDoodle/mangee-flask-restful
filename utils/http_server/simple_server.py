from flask import Blueprint, send_from_directory

server = Blueprint('http_server', __name__, 
                    static_url_path='',
			        static_folder='/web')

@server.route('/', defaults={'path': ''})
@server.route('/<path:path>', methods=['GET'])
def index(path):
	return send_from_directory(directory='web', filename='index.html')

# Should be an option
@server.errorhandler(404)
def resource_not_found(e):
	return index(path='')