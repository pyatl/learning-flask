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
            post.split('/')[1] for post in posts
            ] if post_name not in  ['404.txt', 'index.txt']
        ]

def get_file_contents(filename, feed=False):
    if not feed:
        file_path = f'posts/{filename}'
    else:
        file_path = f'feeds/{filename}'

    file_path = os.path.join(BASE_DIR, file_path )
    with open(file_path, 'r') as f:
        return f.read()

@app.route('/')
def index():
    content = get_file_contents('index.txt')
    return render_template('post.html', content=content, posts=list_posts())

@app.route('/posts/<post_name>', methods=['GET'])
def post(post_name):
    try:
        content = get_file_contents(f'{post_name}.txt')
    except:
        content = get_file_contents('404.txt')
    
    return render_template('post.html', content=content)

### static feeds

CATS_FEED_DATA = get_file_contents('cat-facts.json', feed=True)

@app.route('/feed/cat-facts', methods=['GET'])
def cat_feed():
    return CATS_FEED_DATA

BLS_FEED_DATA = get_file_contents('bls.csv', feed=True)

@app.route('/feed/bls', methods=['GET'])
def bls_feed():
    return BLS_FEED_DATA
    