from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

## CONFIG

app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

## DB -> Models
class Question(db.Model):
    pass


class Answer(db.Model):
    pass


## ROUTE
@app.route("/")
def index():
    pass


app.run(debug=True)
