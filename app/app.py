#!/usr/bin/python3
from flask import Flask
from flask_restful import Api, Resource
import socket
import os
import uuid

os.environ["AUTHOR"] = "Anton Sokolov"
os.environ["UUID"] = str(uuid.uuid4())

app = Flask(__name__)
api = Api()

class Hostname(Resource):
    def get(self):
        return (socket.gethostname())


class Author(Resource):
    def get(self):
        return(os.environ.get("AUTHOR", ''))
     


class Uuid(Resource):
    def get(self):
        return(os.environ.get("UUID", ''))
        
     
api.add_resource(Uuid, "/id")
api.add_resource(Hostname, "/hostname")
api.add_resource(Author, "/author")

api.init_app(app)
if __name__ == '__main__':
    app.run(debug=True, host = '0.0.0.0', port=8000 )

