
import os 

class Config : 

    """ Base configuration for all environments """
    SECRET_KEY = os.environ.get('SECRET_KEY')
    DEBUG = False 
    TESTING = False 

class DevelopmentConfig( Config ) : 
    """ config for local development """
    DEBUG = True 
    SQLALCHEMY_DATABASE_URI = os.environ.get("DEV_DATABASE_URL" , "sqlite:///dev.db" ) 

class TestingConfig( Config ) : 
    """ config for testing """
    TESTING = True 
    SQLALCHEMY_DATABASE_URI = os.environ.get( 'TEST_DATABASE_URL' , "sqlite:///dev.db")

class ProductionConfig( Config ) :

    """ config for production env """ 
    SQLALCHEMY_DATABASE_URI = os.environ.get('PROD_DATABASE_URL' ) 

