from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow 
from flask_cors import CORS
import os

app = Flask(__name__)
ma = Marshmallow(app)

CORS(app)

basedir = os.getcwd()

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.game')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


from solution import routes