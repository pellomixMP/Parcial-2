import os

class Config:
    
    SQLALCHEMY_DATABASE_URI = 'sqlite:///TasksDB.accdb'
    
    
    SECRET_KEY = '1234'

    
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    STATIC_FOLDER = 'static'

    
    TEMPLATE_FOLDER = 'templates'

    
    SESSION_TYPE = 'filesystem'

   

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False


