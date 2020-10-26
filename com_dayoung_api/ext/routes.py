import logging
from flask import Blueprint
from flask_restful import Api
from com_dayoung_api.resources.home import Home
from com_dayoung_api.resources.movie import Movie, Movies
from com_dayoung_api.resources.user import User, Users, Auth, Access
from com_dayoung_api.resources.review import Review, Reviews

home = Blueprint('home', __name__, url_prefix='/api')
user = Blueprint('user', __name__, url_prefix='/api/user')
users = Blueprint('users', __name__, url_prefix='/api/users')
auth = Blueprint('auth', __name__, url_prefix='/api/auth')
access = Blueprint('access', __name__, url_prefix='/api/access')
review = Blueprint('review', __name__, url_prefix='/api/review')
reviews = Blueprint('reviews', __name__, url_prefix='/api/reviews')

api = Api(home)
api = Api(user)
api = Api(users)
api = Api(auth)
api = Api(article)
api = Api(articles)

def initialize_routes(api):
    api.add_resource(Home, '/api')
    api.add_resource(Movie, '/api/item/<string:id>')
    api.add_resource(Movies, '/api/items')
    api.add_resource(User, '/api/user/<string:id>')
    api.add_resource(Users, '/api/users')
    api.add_resource(Auth, '/api/auth')
    api.add_resource(Access, '/api/access')
    api.add_resource(Review, '/api/review')
    api.add_resource(Reviews, '/api/reviews')
    
@user.errorhandler(500)
def user_api_error(e):
    logging.exception('An error occured during user request. %s' % str(e))