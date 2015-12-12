from flask_crud import app
from flask import render_template, request, url_for,redirect,flash,session
from models import User, bcrypt
import logging
from logging.handlers import RotatingFileHandler

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
        users = User.query.filter_by(username=request.form['username']).first()
        if users is not None and bcrypt.check_password_hash(
        users.password,request.form['password']):
        #if request.form['username'] == 'admin' and request.form['password'] == 'admin':
            session['username'] = request.form['username']
            return redirect(url_for('index'))
        else:
            error = "Incorrect User and Password"
            app.logger.warning('Incorrect passwword for username (%s)',
                                request.form.get('username'))
    return render_template('login.html',error=error)

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
