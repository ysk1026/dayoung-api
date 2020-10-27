from flask_restful import Resource, reqparse
from com_dayoung_api.ext.db import db, openSession
from com_dayoung_api.resources.user import UserDto
from com_dayoung_api.resources.movie import MovieDto

class ReviewDto(db.Model):
    __tablename__ = "reviews"
    __table_args__ = {'mysql_collate':'utf8_general_ci'}
    
    rev_id: int = db.Column(db.Integer, primary_key=)
    title: str = db.Column(db.String(100))
    content: str = db.Column(db.String(500))
    label: int = db.Column(db.Integer(10))
     
    user_id: str = db.Column(db.String(30), db.ForeignKey(UserDto.user_id))
    movie_id: int = db.Column(db.Integer, db.ForeignKey(MovieDto.movie_id))
    
    def __init__(self, title, content, label, user_id, movie_id):
        self.title = title
        self.content = content
        self.label = label
        self.user_id = user_id
        self.movie_id = movie_id
        
    def __repr__(self):
        return f'rev_id = {self.rev_id}, user_id = {self.user_id}, movie_id = {self.movie_id},\
            title = {self.title}, content = {self.content}, label = {self.label}'
    
    @property
    def json(self):
        return {
            'rev_id' : self.rev_id,
            'user_id' : self.user_id,
            'movie_id' : self.movie_id,
            'title' : self.title,
            'content' : self.content
        }
        
class ReviewDao(ReviewDto):
    
    @classmethod
    def find_all(cls):
        return cls.query.all()
    
    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name == name)
    
    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id == id).first()
    
    @staticmethod
    def save(review):
        Session = openSession()
        session = Session()
        newArticle = ReviewDto(title = review['title'],
                                content = review['content'],
                                user_id = review['user_id'],
                                movie_id = review['movie_id'])
        
        session.add(newArticle)
        session.commit()
        
    @staticmethod
    def modify(review):
        Session = openSession()
        session = Session()
        session.add(review)
        session.commit()
        
    @classmethod
    def delete(cls,rev_id):
        Session = openSession()
        session = Session()
        data = cls.query.get(rev_id)
        session.delete(data)
        session.commit()
        
# ==============================================================
# ==============================================================
# ====================        API       ========================
# ==============================================================
# ==============================================================

parser = reqparse.RequestParser()
parser.add_argument('user_id', type =int, required =False, help ='This field cannot be left blank')
parser.add_argument('movie_id', type =int, required =False, help ='This field cannot be left blank')
parser.add_argument('title', type =str, required =False, help ='This field cannot be left blank')
parser.add_argument('content', type =str, required =False, help ='This field cannot be left blank')

class Review(Resource):
    
    @staticmethod
    def post():
        args = parser.parge_args()
        review = ReviewDto(args['title'], args['content'], \
            args['user_id'], args['movie_id'])
        
        try:
            ReviewDao.save(args)
            return {'code' : 0, 'message' : 'SUCCESS'}, 200
        except:
            return {'message' : 'An error occured inserting the review'}, 500
        
    def get(self, id):
        review = ReviewDao.find_by_id(id)
        if review:
            return review.json()
        return {'message' : 'Article not found'}, 404
    
    def put(self, id):
        data = Review.parser.parse_args()
        review = ReviewDao.find_by_id(id)
        
        
        