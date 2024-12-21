from datetime import datetime
import random
import string
from flask import Flask, jsonify, render_template, request
from flask_login import LoginManager, current_user, login_required
from flask_cors import CORS
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from website.models import User, user_db, book_db
from website.views import views
from website.auth import auth
from website.admin import admin

# def create_app():
app = Flask(__name__)
app.config["SECRET_KEY"] = "ytfyfyt wajhfjawf"
CORS(app, resources={r"/*": {"origins": "https://flask-lib-system.vercel.app/"}})


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


def generate_random_code(length):
    characters = string.ascii_letters + string.digits  # 使用字母和数字
    random_code = "".join(random.choice(characters) for _ in range(length))
    return random_code


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/barcode")
@login_required
def barcode():
    return render_template("barcode.html")


@app.route("/door")
@login_required
def door():
    return render_template("door.html")


@app.route("/profile")
@login_required
def profile():
    return render_template("profile.html")


@app.route("/emulator")
@login_required
def emulator():
    return render_template("emulator.html")


@app.route("/getDoor")
@login_required
def getdoor():
    user = user_db.check_item(current_user.id)
    random_code = generate_random_code(50)
    user["random_code"] = random_code
    user["activate"] = True
    user["time"] = datetime.now()
    user_db.create_item(user)
    return jsonify(user["_id"] + " " + random_code)


@app.route("/getUser")
@login_required
def getUser():
    return {"message": "success", "data": current_user.get_user()}


@app.route("/checkBook", methods=["POST"])
@login_required
def checkdata():
    barcode = request.form.get("barcode")  # 获取表单字段 sk 的值
    print(barcode)
    respond = book_db.check_item(barcode)
    if respond:
        return {"message": "success", "data": respond}
    return {"message": "id doesn't exist"}


# return app


if __name__ == "__main__":
    app.run(debug=True)
