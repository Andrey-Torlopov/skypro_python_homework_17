from run import app, db
from flask_restx import Api, Resource
from app.database import *


api = Api(app)
movies_ns = api.namespace('movies')
directors_ns = api.namespace('directors')
genre_ns = api.namespace('genres')


@movies_ns.route('/')
class MoviesView(Resource):
    def get(self):
        return "OK", 200


print("ok...")