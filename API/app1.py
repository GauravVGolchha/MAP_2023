from flask import Flask
app = Flask(__name__)


@app.route('/hi')
def hello():
    return "Hello there!"

@app.route('/')
def home():
    return "Hey there, you need to apply /user or /user/Name or /todos or /todos/todoid at last in URL for getting details of user or todolist!"


app.run(debug=True)



#https://docs.github.com/en/rest
#https://codeburst.io/this-is-how-easy-it-is-to-create-a-rest-api-8a25122ab1f3
