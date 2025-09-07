from app import app

# import render_template() helper function from flask framework 
# that use jinja2 engine to render html tempalates and send them to the client 

from flask import render_template 
from datetime import datetime

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
    return render_template( "index.html" , title= "Insight" , current_year = current_year , user=user , posts=posts )