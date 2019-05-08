# Import flask and template operators
from flask import Flask, Response
# from pymongo import MongoClient
from flask_cors import CORS
import json

# Define the WSGI application object
app = Flask(__name__, static_url_path='')
# Configurations
app.config.from_object('config')
CORS(app, supports_credentials=True)

# SET UP DB
# client = MongoClient("mongodb://kay:myRealPassword@mycluster0-shard-00-00.mongodb.net:27017,mycluster0-shard-00-01.mongodb.net:27017,mycluster0-shard-00-02.mongodb.net:27017/admin?ssl=true&replicaSet=Mycluster0-shard-0&authSource=admin")
# db = client.test

# client = MongoClient('mongodb://localhost:27017/')
# db = client['fetch-conv']

@app.route('/', methods=['GET'])
def indexApp():
    return Response(
        json.dumps({
            'data': 'Welcome to locations API'
        }, indent=4, sort_keys=True),
        status=404,
        content_type='application/json'
    )


# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return Response(
        json.dumps({
            'data': 'Not found'
        }, indent=4, sort_keys=True),
        status=404,
        content_type='application/json'
    )

# Import a module / component using its blueprint handler variable (mod_auth)
from src.routes import locations as locations_module

# Register blueprint(s)
app.register_blueprint(locations_module)
# app.register_blueprint(xyz_module)
# ..
