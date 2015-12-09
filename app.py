from flask import Flask, render_template, request, url_for,redirect

app = Flask(__name__)

@app.route('/')
def index():
    return 'R2D2'

@app.route('/login',methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        if request.form['username'] == 'admin' and request.form['password'] == 'admin':
            return render_template(('base.html'))
        else:
            return "Inconrrect user and password"
    return render_template('login.html')

@app.route('/user/<name>')
def user(name):
    return name

@app.route('/post/<int:post_id>')
def post(post_id):
    return 'Post %d' % post_id


if __name__ == "__main__":
    app.debug = True
    app.run()
