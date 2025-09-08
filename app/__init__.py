# import Flask class from flask package that we gonna use to create app instance 
from flask import Flask 
# import Config class from config module that we gonna use to configure our app
from config import Config

# create app object as an instance of Flask class 
# passing __name__ predifined python variable that contain the name of current module ( app/__init__ )
# __name__ variable is useful to set root folder for this project 
# the folder ( app/ ) that flask will use as current folder and load static template files 

app = Flask( __name__ )

# set the secret key for our flask app using Config class 
# that set SECRET_KEY from our environement variables  

app.config.from_object( Config )
# import from app package the routes module 

from app import routes 