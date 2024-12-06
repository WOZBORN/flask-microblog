from flask import Flask, g
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, current_user

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flaskr.sqlite'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['WTF_CSRF_ENABLED'] = False  # CSRF включён по умолчанию

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    @login_manager.user_loader
    def load_user(user_id):
        """Загружает пользователя по user_id."""
        from flaskr.models import User
        return User.query.get(int(user_id))

    @app.before_request
    def before_request():
        g.user = current_user  # Устанавливаем текущего пользователя в g.user

    with app.app_context():
        db.create_all()

    from flaskr.routes import blog
    from flaskr.routes import auth
    app.register_blueprint(auth.bp)
    app.register_blueprint(blog.bp)

    return app
