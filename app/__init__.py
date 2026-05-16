from flask import Flask
from dotenv import load_dotenv
from config import Config
from .extensions import db, login_manager, bcrypt, migrate

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    from . import models

    # Initialize Extensions
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    login_manager.login_message_category = 'error'

    @login_manager.user_loader
    def load_user(user_id):
        from app.models import User
        return db.session.get(User, int(user_id))

    # Register blueprints
    from app.auth import auth_bp
    from app.notes import notes_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(notes_bp, url_prefix='/notes')

    return app

