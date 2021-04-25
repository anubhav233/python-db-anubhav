import os

from flask import request, jsonify
from flask_cors import CORS

from project import create_app
from project.models import db


app = create_app('flask.cfg')

HOST = '0.0.0.0'
PORT = '8080'
DEBUG = True

if __name__ == '__main__':
    app.run(host=HOST, port=PORT, debug=DEBUG)
