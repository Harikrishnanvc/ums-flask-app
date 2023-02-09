import environ
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

env = environ.Env()
environ.Env.read_env()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = env('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

migrate = Migrate(app, db)

from core.user_app import views, models
from .user_app import user_app
from core import swagger

app.register_blueprint(user_app)
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5432)
