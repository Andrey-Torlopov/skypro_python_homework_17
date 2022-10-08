from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from app.main_api import *

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


@app.route('/')
def main():
    return 'Homework #17'

def setup_database():
    db.drop_all()
    db.create_all()


if __name__ == '__main__':
    app.run(debug=False)
    setup_database()

