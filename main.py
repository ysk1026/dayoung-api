from flask import Flask
from flask_restful import Api
from flask_cors import CORS

print('===== 1 =====')
app = Flask(__name__)
CORS(app)

