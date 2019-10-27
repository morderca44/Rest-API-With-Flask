import os

from flask import Flask
from flask_jwt import JWT
from flask_restful import Api

from resources.item import Item, ItemList
from resources.user import UserRegister
from security import authenticate, identity
from resources.store import Store, StoreList

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL", 'sqlite:///data.db') #  oznacza to że sqlalchemy "przesiaduje" w bazie sqlite, environ ma dwa paramery, jeden dla DB w heroku
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'jose'
api = Api(app)

# app.config['JWT_AUTH_URL_RULE'] = '/login' # zmienia end point na /login z defaultowego /auth
jwt = JWT(app, authenticate, identity) # /auth
# config JWT to expire within half an hour
# app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds = 1800)
# config JWT auth key name to be 'email' instead of default 'username'
# app.config['JWT_AUTH_USERNAME_KEY'] = 'email'


api.add_resource(Item,"/item/<string:name>")
api.add_resource(ItemList,"/items")
api.add_resource(UserRegister, "/register")
api.add_resource(Store, "/store/<string:name>")
api.add_resource(StoreList, "/stores")


if __name__ == "__main__":
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True) # if pozwala na nie odpalenie app.run przy imporcie z app.py