"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
import random
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from models import db
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)

# Handle/serialize errors like a JSON object
class Family:

    def __init__(self, last_name):
        self.last_name = last_name
        # example list of members
        self._members = [
            {
            "id": self._generateId(),
            "first_name": "John",
            "last_name": "Doe",
            "age": "33",
            "genre": "Male",
            "lucky_numbers": "7, 13, 22"
            },
            {
            "id": self._generateId(),
            "first_name": "Jane",
            "last_name": "Doe",
            "age": "35",
            "genre": "Female",
            "lucky_numbers": "10, 14, 03"
            },
            {
            "id": self._generateId(),
            "first_name": "Jimmy",
            "last_name": "Doe",
            "age": "5",
            "genre": "Male",
            "lucky_numbers": "1"
            },
        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return random.randint(0, 99999999)

    def add_member(self, member):
        ## you have to implement this method
        ## append the member to the list of _members
        pass

    def delete_member(self, id):
        ## you have to implement this method
        ## loop the list and delete the member with the given id
        pass

    def update_member(self, id, member):
        ## you have to implement this method
        ## loop the list and replace the memeber with the given id
        pass

    def get_member(self, id):
        ## you have to implement this method
        ## loop all the members and return the one with the given id
        pass

    def get_all_members(self):
        return self._members

doe_family = Family("Doe")

# generate sitemap with all your endpoints
@app.route('/members')
def handleall():
    resp = {
        "members": doe_family.get_all_members(),
        "family_name": doe_family.last_name,
        "lucky_numbers": doe_family.
    }

    return jsonify(resp), 200

@app.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "hello": "world"
    }

    return jsonify(response_body), 200

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
