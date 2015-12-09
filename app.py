from flask import Flask, render_template, request, url_for,redirect,flash,session
import logging
from logging.handlers import RotatingFileHandler

app = Flask(__name__)

@app.route('/')
def index():
    if 'username' in session:
        return render_template('home.html')
    else:
        return redirect(url_for('login'))


@app.route('/login',methods=['POST', 'GET'])
def login():
    error = None
    if request.method == "POST":
        if valid(request.form['username'],request.form['password']):
            session['username'] = request.form['username']
            return redirect(url_for('index'))
        else:
            error = "Inconrrect User and Password"
            app.logger.warning('Incorrect username passwword for user (%s)',
                                request.form.get('username'))
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

@app.route('/logout')
def logout():
    session.pop('username',None)
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.debug = True
    app.secret_key = 'secret!'
    # logging
    handler = RotatingFileHandler('error.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    app.run()
