from flask import Flask
from flask_restful import Api, Resource #new
app = Flask(__name__)
api = Api(app) 							#new

users = [								#new
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

class HelloWorld(Resource):				#new
    def get(self):
        return {'hello': 'world'}

class UserList(Resource):				#new
    def get(self):
        return users,200


@app.route('/hi')
def hello():
    return "Hello there!"

@app.route('/')
def home():
    return "Hey there, you need to apply /user or /user/Name or /todos or /todos/todoid at last in URL for getting details of user or todolist!"


api.add_resource(HelloWorld, '/hello','/greet')			#new
api.add_resource(UserList, '/user')						#new

app.run(debug=True)



#https://docs.github.com/en/rest
#https://codeburst.io/this-is-how-easy-it-is-to-create-a-rest-api-8a25122ab1f3
