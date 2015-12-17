from flask_crud import app, db
from flask import render_template, request, url_for,redirect,flash,session
#from models import User, bcrypt
from form import RegistrationForm,LoginForm
import logging
from logging.handlers import RotatingFileHandler

@app.route('/')
def index():
    if 'username' in session:
        userAll = User.query.all()
        username = []
        email = []
        fullname = []
        index = []
        for u in range(len(userAll)):
            index.append(u+1)
            username.append(userAll[u].username)
            email.append(userAll[u].email)
            fullname.append(userAll[u].fullname)
        return render_template('home.html',query=zip(index,fullname,username,email))
    else:
        return redirect(url_for('login'))

@app.route('/login',methods=['POST', 'GET'])
def login():
    loginError = None
    login = LoginForm()

    ##LOGIN

    if login.validate_on_submit():
        users = User.query.filter_by(username=request.form['username']).first()
        if users is not None and bcrypt.check_password_hash(
        users.password,request.form['password']):
        #if request.form['username'] == 'admin' and request.form['password'] == 'admin':
            session['username'] = request.form['username']
            return redirect(url_for('index'))
        else:
            loginError = "Incorrect User and Password"
            app.logger.warning('Incorrect passwword for username (%s)',
                                request.form.get('username'))
    return render_template('login.html',form1=RegistrationForm(),form2=login,loginError=loginError,registerError=None)


@app.route('/register',methods=['GET','POST'])
def register():

    register = RegistrationForm()
    registerError = None
    if register.validate_on_submit():
        user_unique = User.query.filter_by(username=request.form['username']).first()
        email_unique = User.query.filter_by(email=request.form['email']).first()
        if user_unique is None and email_unique is None:

            user = User(register.fullname.data, register.username.data, register.email.data,
            register.password.data)
            db.session.add(user)
            db.session.commit()
            session['username'] = request.form['username']
            flash("Thank's for registering")
            return redirect(url_for('index'))
        else:
            registerError = "Email or Username already taken"
    return render_template('login.html',form1=register,form2=LoginForm(),loginError=None,registerError=registerError)


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
