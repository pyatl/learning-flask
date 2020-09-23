import os
import glob
from flask import (
    Flask,
    render_template
)

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def list_posts():
    posts = glob.glob(f'posts/*.txt')
    return [
        post_name.split('.')[0] for post_name in [
            post.split('/')[1] for post in posts] if post_name not in  ['404.txt', 'index.txt']
        ]

def get_post_contents(filename):
    file_path = os.path.join(BASE_DIR, f'posts/{filename}')
    with open(file_path, 'r') as f:
        return f.read()

@app.route('/')
def index():
    content = get_post_contents('index.txt')
    return render_template('post.html', content=content, posts=list_posts())

@app.route('/posts/<post_name>', methods=['GET'])
def post(post_name):
    try:
        content = get_post_contents(f'{post_name}.txt')
    except:
        content = get_post_contents('404.txt')
    
    return render_template('post.html', content=content)



