from flask import Flask
from flask_login import LoginManager
from .models import User, user_db
from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "ytfyfyt wajhfjawf"
    CORS(app, resources={r"/*": {"origins": "https://flask-lib-system.vercel.app/"}})

    from .views import views
    from .auth import auth
    from .admin import admin

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")
    app.register_blueprint(admin, url_prefix="/admin")

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        user = user_db.check_item(user_id)
        if user:
            return User(user["_id"], user["name"], user["type"])
        return None

    return app
