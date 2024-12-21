from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user
from .models import user_db, book_db
import random, string
from datetime import datetime


views = Blueprint("views", __name__)


def generate_random_code(length):
    characters = string.ascii_letters + string.digits  # 使用字母和数字
    random_code = "".join(random.choice(characters) for _ in range(length))
    return random_code


@views.route("/")
def home():
    return render_template("home.html")


@views.route("/barcode")
@login_required
def barcode():
    return render_template("barcode.html")


@views.route("/door")
@login_required
def door():
    return render_template("door.html")


@views.route("/profile")
@login_required
def profile():
    return render_template("profile.html")


@views.route("/emulator")
@login_required
def emulator():
    return render_template("emulator.html")


@views.route("/getDoor")
@login_required
def getdoor():
    user = user_db.check_item(current_user.id)
    random_code = generate_random_code(50)
    user["random_code"] = random_code
    user["activate"] = True
    user["time"] = datetime.now()
    user_db.create_item(user)
    return jsonify(user["_id"] + " " + random_code)


@views.route("getUser")
@login_required
def getUser():
    return {"message": "success", "data": current_user.get_user()}


@views.route("/checkBook", methods=["POST"])
@login_required
def checkdata():
    barcode = request.form.get("barcode")  # 获取表单字段 sk 的值
    print(barcode)
    respond = book_db.check_item(barcode)
    if respond:
        return {"message": "success", "data": respond}
    return {"message": "id doesn't exist"}
