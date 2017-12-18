import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel

class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type=str,
        required=True,
        help="This field cannot be blank"
    )
    parser.add_argument('email',
        type=str,
        required=True,
        help="This field cannot be blank"
    )
    parser.add_argument('password',
        type=str,
        required=True,
        help="This field cannot be blank"
    )
    parser.add_argument('firstname',
        type=str
    )
    parser.add_argument('lastname',
        type=str
    )

    def post(self):
        data = UserRegister.parser.parse_args()
        if UserModel.find_by_username(data.username):
            return {'message':'An user with username "{}" already exists.'.format(data.username)}, 400

        user = UserModel(data)

        try:
            user.save_to_db()
        except:
            return {"message":"An error occurred inserting the user."}, 500

        return user.json(), 201
