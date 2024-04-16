import os 
import secrets

class Config:

    def generate_secret_key(length=32) -> str:
        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        random_string = ''.join(secrets.choice(chars) for i in range(length))
        return random_string
    
    # Database URL.
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///database.db'

    # Secret key that guarantees the security of the application.
    SECRET_KEY = os.environ.get('SECRET_KEY') or generate_secret_key()

    # Disable change tracking in SQLAlchemy.
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Maximum size for upload files.
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB

    # Diretory to template files.
    TEMPLATES_FOLDER = '../src/templates/'

    # Diretory to static files.
    STATIC_FOLDER = '../src/static/'

    # Defines that templates must be loaded automatically.
    TEMPLATES_AUTO_RELOAD = True

    # Depuration mode.
    DEBUG = True

