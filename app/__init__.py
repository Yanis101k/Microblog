# import Flask class from flask package that we gonna use to create app instance 
from flask import Flask 
# import Config classes from config module that we gonna use to configure our app
from config import Config , DevelopmentConfig , TestingConfig , ProductionConfig

import os 
# import dotenv package that contain load_dotenv() fuction that load .*env files and use it config variables 
from dotenv import load_dotenv

# create app object as an instance of Flask class 
# passing __name__ predifined python variable that contain the name of current module ( app/__init__ )
# __name__ variable is useful to set root folder for this project 
# the folder ( app/ ) that flask will use as current folder and load static template files 

app = Flask( __name__ )

# import FLASK_ENV variable to let flask know in which env is ( dev , testing , prod ) 
load_dotenv( "../.flaskenv")
env = os.getenv( "FLASK_ENV" )

# load the configuration of current env 
match env : 

    case "development" : app.config.from_object ( DevelopmentConfig ) 

    case "testing" : app.config.from_object( TestingConfig )

    case "production" : app.config.from_object( ProductionConfig )

    case __ : app.config.from_object( Config )


# import from app package the routes module 

from app import routes 

print( app.config )
