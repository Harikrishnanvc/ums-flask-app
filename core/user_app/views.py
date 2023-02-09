import sqlalchemy.orm.exc
from flask import request
from flask.views import MethodView

from core import db
from core.user_app.models import UserDetails


# create users and get user details
class CreateAndListUsers(MethodView):
    methods = ['POST', 'GET']

    def post(self):
        if request.is_json:
            data = request.get_json()
            first_name = data['first_name']
            last_name = data['last_name']
            email = data['email']
            username = data['username']
            password = data['password']
            age = data['age']
            user = UserDetails(first_name=first_name, last_name=last_name, email=email,
                               username=username, password=password, age=age)
            db.session.add(user)
            db.session.commit()
            response = {'message': 'Successfully created', }
        else:
            response = {'error': 'The request payload is not in JSON format', }
        return response

    def get(self):
        users = UserDetails.query.all()
        if not users:
            response = {"message": "Users not found"}
        else:
            response = []
            for user in users:
                users_list = {
                    'id': user.id,
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'username': user.username,
                    'email': user.email,
                    'password': user.password,
                    'age': user.age
                }
                response.append(users_list)

        return response


# delete users
class DeleteView(MethodView):
    methods = ['DELETE']

    def delete(self, pk):
        try:
            user = UserDetails.query.get(pk)
            db.session.delete(user)
            db.session.commit()
            response = {"message": "User deleted successfully"}

        except sqlalchemy.orm.exc.NoResultFound:
            response = {"message": "Invalid User ID"}

        return response
