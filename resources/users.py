from flask_restful import Resource, reqparse
from flask import request
from flask_bcrypt import generate_password_hash, check_password_hash
from models import Users, db

class UserResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', required = True, help = 'Name is required')
    parser.add_argument('phone', required = True, help = 'Phone number is required')
    parser.add_argument('password', required = True, help = 'Password is required')

    # create user method
    def post(self):
        data = self.parser.parse_args()
        print(data)

        # verofy if phone_no exits
        phone = Users.query.filter(Users.phone == data['phone']).first()

        if phone :
            return {
                "message":"Phone number already taken"
            }, 422

        # encrypt password
        hash = generate_password_hash(data['password']).decode()

        user = Users(name = data['name'], phone = data['phone'], password = hash)

        db.session.add(user)
        db.session.commit()


        return {
            "message":"User created successfully",
            "hash":hash
        }



class LoginResource(Resource):
    parser = reqparse.RequestParser()
    # parser.add_arguement('name', requierd = True, help = 'Name is required')
    parser.add_argument('phone', required = True, help = 'Phone number is required')
    parser.add_argument('password', required = True, help = 'Password is required')

    def post(self):
        data = self.parser.parse_args()

        # 1. retrieve the user using usique key
        user = Users.query.filter_by(phone = data['phone']).first()

        # 2.
        if user == None:
            return {"message":"Invalid username or password"}, 401
        
        if check_password_hash(user.password, data['password']):
            # generate fwt

            return {"message":"Login successful",
                     "user": user.to_dict()}, 200
        
        else:
            return {"message":""}, 401

    



