# import Flask class from flask package that we gonna use to create app instance 
from flask import Flask 
# import Config classes from config module that we gonna use to configure our app
from config import Config , DevelopmentConfig , TestingConfig , ProductionConfig

# import SQLAlchemy module for database integration 
from flask_sqlalchemy import SQLAlchemy 

# import Migrate module to handle and keep track of our database migration 
from flask_migrate import Migrate 


# create app object as an instance of Flask class 
# passing __name__ predifined python variable that contain the name of current module ( app/__init__ )
# __name__ variable is useful to set root folder for this project 
# the folder ( app/ ) that flask will use as current folder and load static template files 

app = Flask( __name__ )

import os
from dotenv import load_dotenv

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(BASE_DIR, '..', '.flaskenv'))  # always resolves correctly
env = os.getenv( "FLASK_ENV" )

# load the configuration of current env 
match env : 

    case "development" : app.config.from_object ( DevelopmentConfig ) 

    case "testing" : app.config.from_object( TestingConfig )

    case "production" : app.config.from_object( ProductionConfig )

    case __ : app.config.from_object( Config )



db = SQLAlchemy(app) 

migrate = Migrate( app , db )



# import from app package the routes module 


from app import routes , models
