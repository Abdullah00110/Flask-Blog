import os
from dotenv import load_dotenv
import base64
from flask import Flask, request   
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from email.mime.text import MIMEText
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build


app = Flask(__name__)

load_dotenv()
# Define the OAuth 2.0 scopes
SCOPES = ['https://www.googleapis.com/auth/gmail.send']
CLIENT_SECRETS_FILE = "client_secret.json"

# Configure Flask App
app.config['SECRET_KEY'] = '6a2dd7adefc8975c1afffea5240a1fb7'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Blog.db'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('abdullahcodes123@gmail.com')
app.config['MAIL_PASSWORD'] = os.environ.get('Abd@#123')
mail = Mail(app)
from blog import routes