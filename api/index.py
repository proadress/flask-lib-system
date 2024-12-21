from flask import Flask,render_template
from flask_login import LoginManager
from flask_cors import CORS

# import sys
# import os

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from api.models import User, user_db
from api.views import views
from api.auth import auth
from api.admin import admin

# def create_app():
app = Flask(__name__)
app.config["SECRET_KEY"] = "ytfyfyt wajhfjawf"
CORS(app, resources={r"/*": {"origins": "https://flask-lib-system.vercel.app/"}})


# app.register_blueprint(views, url_prefix="/")
# app.register_blueprint(auth, url_prefix="/")
# app.register_blueprint(admin, url_prefix="/admin")


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return "About"


login_manager = LoginManager()
login_manager.login_view = "auth.login"
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    user = user_db.check_item(user_id)
    if user:
        return User(user["_id"], user["name"], user["type"])
    return None


# return app
