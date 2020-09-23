from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/cheese')
def cheese():
    return 'say cheese'


@app.route('/hello/<name>')
def say_hello(name):
    return f'Hello, {name}'


@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'post id: {post_id}'