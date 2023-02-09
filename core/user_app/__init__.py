from flask import Blueprint

user_app = Blueprint('user_app', __name__, url_prefix='/user-app')

from . import views, models, urls
