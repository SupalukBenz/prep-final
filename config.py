import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = "you-will-never-guess"
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "radii.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TEMPLATES_AUTO_RELOAD = True
