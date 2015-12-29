from crud import app, db
from flask import render_template, request, url_for,redirect,flash,session
from models import User, Post,bcrypt
from form import RegistrationForm,LoginForm,PostForm,UpdateForm
import logging
from logging.handlers import RotatingFileHandler
from flask.ext.login import login_required,logout_user,login_user,current_user
from datetime import datetime

@app.route('/')
@login_required

def index():
    userAll = User.query.all()
    username = []
    email = []
    fullname = []
    index = []
    userlog = current_user
    for u in range(len(userAll)):
        index.append(u+1)
        username.append(userAll[u].username)
        email.append(userAll[u].email)
        fullname.append(userAll[u].fullname)
    return render_template('home.html',query=zip(index,fullname,username,email),userlog=userlog)

@app.route('/login',methods=['POST', 'GET'])
def login():
    loginError = None
    login = LoginForm()
    ##LOGIN

    if login.validate_on_submit():
        users = User.query.filter_by(username=login.username.data).first()
        print users
        if users:
            if bcrypt.check_password_hash(users.password,login.password.data):
                login_user(users)
                flash("You were logged in")
                return redirect(url_for('index'))
        else:
            loginError = "Incorrect User and Password"
            app.logger.warning('Incorrect passwword for username (%s)',
                                login.username.data)
    return render_template('login.html',form1=RegistrationForm(),form2=login,loginError=loginError,
    registerError=None)


@app.route('/register',methods=['GET','POST'])
def register():

    register = RegistrationForm()
    registerError = None
    if register.validate_on_submit():
        user_unique = User.query.filter_by(username=register.username.data).first()
        email_unique = User.query.filter_by(email=register.email.data).first()
        if user_unique is None and email_unique is None:

            user = User(register.fullname.data, register.username.data, register.email.data,
            register.password.data)
            db.session.add(user)
            db.session.commit()
            login_user(user)
            flash("Thank's for registering")
            return redirect(url_for('index'))
        else:
            registerError = "Email or Username already taken"
    return render_template('login.html',form1=register,form2=LoginForm(),loginError=None,registerError=registerError)


@app.route('/user',methods=["GET","POST"])
def user():
    postForm = PostForm()
    postError = None
    userlog = current_user
    if postForm.validate_on_submit():
        post = Post(postForm.body.data,datetime.utcnow(),userlog.id)
        db.session.add(post)
        db.session.commit()
        flash("Posted")
    else:
        postError = "Write something!"

    return render_template('user.html',userlog=userlog,postForm=postForm,error=postError,showPost=posted(),updateForm=UpdateForm())

def posted():
        userlog = current_user
        u = User.query.get(userlog.id)
        posted = u.posts.all()
        return posted

@app.route('/update',methods=["GET","POST"])
def update():
    updateForm = UpdateForm()
    userlog = current_user
    if updateForm.validate_on_submit():
        user = User.query.get(userlog.id)
        user.fullname=updateForm.fullname.data
        user.phone=updateForm.phone.data
        user.location=updateForm.location.data
        user.website=updateForm.website.data
        user.about_me=updateForm.about.data
        db.session.add(user)
        db.session.commit()
        flash('Your changes have been saved.')
    else:
        user = User.query.filter_by(id=userlog.id)
        updateForm.fullname.data = user.fullname
        updateForm.phone.data = user.phone
        update.location.data = user.location
        updateForm.website.data = user.website
        updateForm.about.data = user.about

    return render_template('user.html',userlog=userlog,postForm=PostForm(),showPost=posted(),updateForm=updateForm)


@app.route('/post/<int:post_id>')
def post(post_id):
    return 'Post %d' % post_id

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))
