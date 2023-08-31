# Using flask restful api
from flask import Flask
from flask_restful import Resource, Api, request, reqparse

# creating flask app
app = Flask(__name__)   
# creating an API object
api = Api(app)

# creating a local database
database = [
    {
        'unique_id':1,
        'name':'admin',
        'occupation':'admin'
    }
]

# using request parser to access the incoming arguements  
user_post_args = reqparse.RequestParser()
# defining the possible arguements
user_post_args.add_argument("name",type=str,help="Name is required. ",required = True)
user_post_args.add_argument("occupation",type=str,help="Name is required. ",required = True)


# defining classes for a particular resource

# UserList - to get the details present in the entire database
class UserList(Resource):
    def get(self):
        return database

# User -  user specific details | methods: GET, POST, PUT, DELETE 
class User(Resource):
    # GET method
    def get(self,unique_id):
        for user in database:
            if(user['unique_id'] == unique_id):
                return user,200
        return "User Not Found",404     
    
    # POST method
    def post(self,unique_id):
        data = user_post_args.parse_args()        
        for user in database:
            if(user['unique_id'] == unique_id):
                return "User already exist !",400

        user = {
            "unique_id":unique_id,
            "name":data['name'],
            "occupation":data['occupation']
        }
        database.append(user)
        return user,201
    
    # PUT
    def put(self,unique_id):
        data = user_post_args.parse_args()        
        for user in database:
            if(user['unique_id'] == unique_id):
                user['name'] = data['name']
                user['occupation'] = data['occupation']
                return user, 200
        user = {
            "unique_id":unique_id,
            "name":data['name'],
            "occupation":data['occupation']
        }
        database.append(user)
        return user,201
    
    # DELETE
    def delete(self,unique_id):
        global database
        database = [user for user in database if user['unique_id'] != unique_id]
        return "User deleted successfully !!",200 

# default routing
@app.route('/')
def home():
    return "Hey there, you need to apply /user to get all user details and /user/any_number with the required arguements to add a new user similarly for delete and put !"

# Adding the api's
api.add_resource(UserList, '/user', '/users', '/userlist','/user/')
api.add_resource(User, '/user/<int:unique_id>')


if __name__ == '__main__':
    app.run(debug=True)       