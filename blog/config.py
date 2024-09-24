import os
# from dotenv import load_dotenv

# load_dotenv()

class Config:

        SECRET_KEY= '6a2dd7adefc8975c1afffea5240a1fb7'
        SQLALCHEMY_DATABASE_URI='sqlite:///Blog.db'
        MAIL_SERVER = 'smtp.googlemail.com'
        MAIL_PORT = 587
        MAIL_USE_TLS = True
        MAIL_USERNAME = os.environ.get('EMAIL_USER')
        MAIL_PASSWORD = os.environ.get('EMAIL_PASS')