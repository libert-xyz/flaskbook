from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'R2D2'

@app.route('/login')
def login():
    return 'Please Log In'

@app.route('/user/<name>')
def user(name):
    return name

@app.route('/post/<int:post_id>')
def post(post_id):
    return 'Post %d' % post_id


if __name__ == "__main__":
    app.debug = True
    app.run()
