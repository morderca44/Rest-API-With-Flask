#resources to zewnętrzna reprezentacja aplikacji z którą kontakt ma klient, jest wspomagana przez paczki z models

from flask_restful import Resource, reqparse
from models.user import UserModel


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!")

    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!")
    def post(self):
        data = UserRegister.parser.parse_args() # użycie powyższego parsera

        if UserModel.find_by_user_name(data['username']):
            return {"message": "user with that username already exists"}, 400

        user = UserModel(**data)
        user.safe_to_db()


        return {"message": "User created successfully"}, 201



