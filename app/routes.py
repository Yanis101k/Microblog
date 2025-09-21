from app import app

# import render_template() helper function from flask framework 
# that use jinja2 engine to render html tempalates and send them to the client 

from flask import render_template , flash , redirect , url_for
from datetime import datetime

from app.forms import LoginForm
# here we map two urls to greet function that return a string using function decorators 
# if the client request "/" or "/index" url this view function will be sent to the client as response  
@app.route("/")
@app.route("/index")
def index() :
    user = { 'username' : 'Yanis' }
    
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
    return render_template( "index.html" , title= "Home" , current_year = current_year , user=user , posts=posts )

@app.route('/login' , methods=['GET' , 'POST' ])
def login() :
    form = LoginForm()

    if form.validate_on_submit() : 
       flash( f'Login requested for user { form.username.data } , remember_me { form.remember_me.data }')
       return redirect( url_for('index') )

    return render_template( "login.html" , form=form , title="Sign-in" , current_year = datetime.now().year )