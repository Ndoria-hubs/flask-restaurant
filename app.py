import os
from flask import Flask, request
from flask_migrate import Migrate
from dotenv import load_dotenv
from flask_restful import Resource, Api
from flask_cors import CORS
from flask_bcrypt import Bcrypt

from models import db, Menu,Category
from resources.category import CategoryResource
from resources.users import UserResource, LoginResource


### import config from .env
load_dotenv()

# 1. >>> create flask instance
app = Flask(__name__)
#setup cors
CORS(app)

#setup flask-restful
api = Api(app)

#setup bcrypt
bcrypt = Bcrypt(app)

# configuring flask thru config object (dict)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL")
# allow sqlalchmey to display/generate sql on terminal
app.config['SQLALCHEMY_ECHO'] = True

# create the migrate object to manage migrations
migrate = Migrate(app, db)

# link our db to the flask instance
db.init_app(app)


#   ------------------------------ #

# @app.get('/')
# def index():
#     # route logic
#     return {'message':'Welcome to my restaurant app'}


class Index(Resource):
    # class method
    def get(self):
        return {'message':"Welcome to my restaurant app"}


@app.get('/menus')
def get_menus():
    menus = Menu.query.all()
    results = []
    for menu in menus:
        results.append(menu.to_dict())
    return results    


@app.post('/menus')
def create_menu():
    data = request.json        

    # create a new instaance with the values sent
    menu = Menu(name = data('name'), price = data('price'))
    db.seshion.add(menu)
    db.session.commit()
    print(data)

    return {
        "message":"Menu  created successfully",
        "menu": menu.to_dict()
    }

# @app.get('/categories/<id>')
# def get_category(id):
#     category = Category.query.filter_by(id = id).first()

#     if category == None:
#         return { "message": "Category not found" }, 404

#     return category.to_dict(rules=('-menus.category',))



api.add_resource(Index, '/')
"""
The second route is going to facilitate GET(single), PATCH, DELETE
PATCH -> 
DELETE -> 
GET one ->
"""
api.add_resource(CategoryResource, '/categories', '/categories/<id>')
api.add_resource(UserResource, '/User')
api.add_resource(LoginResource, '/Login')