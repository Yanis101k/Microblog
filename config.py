
import os 

class Config : 

    """ Base configuration for all environments """
    SECRET_KEY = os.environ.get('SECRET_KEY')
    DEBUG = False 
    TESTING = False 

class DevelopmentConfig( Config ) : 
    """ config for local development """
    DEBUG = True 
    DATABASE_URL = os.environ.get('DEV_DATABASE_URL')

class TestingConfig( Config ) : 
    """ config for testing """
    TESTING = True 
    DATABASE_URL = os.environ.get( 'TEST_DATABASE_URL' )

class ProductionConfig( Config ) :

    """ config for production env """ 
    DATABASE_URL = os.environ.get('PROD_DATABASE_URL') 

