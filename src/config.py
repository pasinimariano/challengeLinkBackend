from dotenv import dotenv_values
from os import environ

ENV = dotenv_values('.env')


class Config:
    SECRET_KEY = ENV['SECRET_KEY']
    SESSION_COOKIE_NAME = environ.get('SESSION_COOKIE_NAME')
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'


class ProdConfig(Config):
    ENV = 'production'
    DEBUG = False
    TESTING = False


class DevConfig(Config):
    ENV = 'development'
    DEBUG = True
    TESTING = True

