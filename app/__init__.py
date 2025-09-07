# import Flask class from flask package that we gonna use to create app instance 
from flask import Flask 

# create app object as an instance of Flask class 
# passing __name__ predifined python variable that contain the name of current module ( app/__init__ )
# __name__ variable is useful to set root folder for this project 
# the folder ( app/ ) that flask will use as current folder and load static template files 

app = Flask( __name__ )

# import from app package the routes module 

from app import routes 