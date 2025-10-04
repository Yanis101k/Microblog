from app import app

# import render_template() helper function from flask framework 
# that use jinja2 engine to render html tempalates and send them to the client 

from flask import render_template , flash , redirect , url_for , request
from urllib.parse import urlsplit
from datetime import datetime

from app.forms import LoginForm , RegistrationForm

from flask_login import current_user , login_user , logout_user , login_required
import sqlalchemy as sa 
from app import db 
from app.models import User 

# here we map two urls to greet function that return a string using function decorators 
# if the client request "/" or "/index" url this view function will be sent to the client as response  
@app.route("/")
@app.route("/index")
@login_required
def index() :
    
    current_year = datetime.now().year
    posts = [
        { 
           'author' : { 'username' : 'kenza'}  , 
           'body' : " i'm wrting blog post about makeup "
        } , 

        {
            'author' : { 'username' : 'abdlghani' } ,
            'body' : " i'm writing a blog post about plaster ball "

        }

    ]
    return render_template( "index.html" , title= "Home" , current_year = current_year  , posts=posts )

@app.route('/login' , methods=['GET' , 'POST' ])
def login() :
    form = LoginForm()

    if current_user.is_authenticated :
        return ( url_for('index'))
     
    form = LoginForm() 

    if form.validate_on_submit() : 
        user = db.session.scalar( ( sa.select(User).where(User.username == form.username.data )))
        if user is None or  user.check_password( form.password.data ) == False : 
            flash('Invalid username or password ')
            return redirect( url_for('login'))
        login_user( user , remember=form.remember_me.data )
        next_page = request.args.get('next')
        print( next_page )

        if not next_page or urlsplit( next_page).netloc != '' :
            next_page = url_for('index')

        return redirect( next_page )    
    return render_template( "login.html" , form=form , title="Sign-in" , current_year = datetime.now().year )


@app.route('/logout') 
def logout() : 
    logout_user()
    return redirect( url_for('index') )  

@app.route('/register' , methods = ["GET" , "POST"])
def register() : 
    
    if current_user.is_authenticated : 
        return url_for( url_for( 'index' ))
    
    form = RegistrationForm()

    if form.validate_on_submit() : 
        
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    
    return render_template('register.html', title='Register', form=form)
