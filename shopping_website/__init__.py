from flask import Flask
from flask_login import LoginManager
from werkzeug.utils import secure_filename
"""
from flask_mail import Mail
from dbconnect import connection
from MySQLdb import escape_string as thwart
import hashlib
import gc
from functools import wraps
"""
UPLOAD_FOLDER = 'shopping_website/static/images/'                             # 저장위치는 run.py 기준!
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from shopping_website import routes