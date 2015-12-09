from flask import Flask, render_template, request, url_for,redirect,flash

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/login',methods=['POST', 'GET'])
def login():
    error = None
    if request.method == "POST":
        if valid(request.form['username'],request.form['password']):
            return redirect(url_for('index'))
        else:
            error = "Inconrrect User and Password"
    return render_template('login.html',error=error)

def valid(user,pasw):
    if user == pasw:
        return True
    else:
        False
@app.route('/user/<name>')
def user(name):
    return name

@app.route('/post/<int:post_id>')
def post(post_id):
    return 'Post %d' % post_id


if __name__ == "__main__":
    app.debug = True
    app.run()
