from flask import Flask
from flask_restful import Api, Resource, reqparse, request

app = Flask(__name__)
api = Api(app)

todos = {}

users = [
    {
        "name": "Nicholas",
        "age": 42,
        "occupation": "Network Engineer"
    },
    {
        "name": "Elvin",
        "age": 32,
        "occupation": "Doctor"
    },
    {
        "name": "Jass",
        "age": 22,
        "occupation": "Web Developer"
    }
]

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

class UserList(Resource):
    def get(self):
        return users,200

class User(Resource):
    def get(self,name):
        for user in users:
            if(name == user["name"]):
                return user, 200
        return "User not found", 404

    def post(self,name):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()

        for user in users:
            if(name == user["name"]):
                return "User with name {} already exists".format(name), 400

        user = {
            "name": name,
            "age": args["age"],
            "occupation": args["occupation"]
        }
        users.append(user)
        return user, 201

    def put(self,name):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()

        for user in users:
            if(name == user["name"]):
                user["age"] = args["age"]
                user["occupation"] = args["occupation"]
                return user, 200
        
        user = {
            "name": name,
            "age": args["age"],
            "occupation": args["occupation"]
        }
        users.append(user)
        return user, 201

    def delete(self,name):
        global users
        users = [user for user in users if user["name"] != name]
        return "{} is deleted.".format(name), 200
      

class TodoSimple(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def post(self, todo_id):
        todos[todo_id] = request.form['task']
        return {todo_id: todos[todo_id]}

class TodoList(Resource):
    def get(self):
        return todos, 200



@app.route('/hi')
def hello():
    return "Hello there!"

@app.route('/')
def home():
    return "Hey there, you need to apply /user or /user/Name or /todos or /todos/todoid at last in URL for getting details of user or todolist!"


api.add_resource(HelloWorld, '/hello','/greet')
api.add_resource(User, "/user/<string:name>")
api.add_resource(UserList, '/user')
api.add_resource(TodoList, '/todos')
api.add_resource(TodoSimple, '/todos/<string:todo_id>','/<string:todo_id>')
app.run(debug=True)


#curl http://localhost:5000/todo1 -d "task=pay the electricity bill" -X PUT
#curl http://localhost:5000/todo2 -d "task=recharge mobile" -X PUT
#curl http://localhost:5000/todo3 -d "task=vehicle servicing due" -X PUT
#https://docs.github.com/en/rest
#https://codeburst.io/this-is-how-easy-it-is-to-create-a-rest-api-8a25122ab1f3
