from flask import Blueprint, render_template, request, redirect, url_for
from datetime import datetime
from werkzeug.security import generate_password_hash
from flask_login import login_required, current_user

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from api.models import user_db


admin = Blueprint("admin", __name__)


@admin.route("/delete", methods=["POST"])
@login_required
def delete_data():
    id = request.form.get("sid").lower()  # 获取表单字段 sk 的值
    respond = user_db.delete_item(id)
    return {"message": respond}


@admin.route("/check", methods=["POST"])
@login_required
def check_data():
    id = request.form.get("sid").lower()  # 获取表单字段 sk 的值
    respond = user_db.check_item(id)
    if respond:
        return {"message": "success", "data": respond}
    return {"message": "id doesn't exist"}


@admin.route("/signup", methods=["POST"])
@login_required
def signup():
    print(request.form)
    user = {
        "_id": request.form.get("sid").lower(),
        "name": request.form.get("username"),
        "password": generate_password_hash(request.form.get("password")),
        "activate": False,
        "time": datetime.now(),
        "type": request.form.get("type"),
    }
    respond = user_db.create_new_item(user)
    return {"message": respond}


@admin.route("/qrpost", methods=["POST"])
@login_required
def qrpost():
    text = request.form.get("random_code")
    text = text.split(" ")
    print(text)
    if len(text) == 2:
        try:
            sid = text[0]
            user = user_db.check_item(sid)
            if user["random_code"] != text[1]:
                return {"message": "wrong key"}
            if user["activate"] == False:
                return {"message": "key expired"}
            user["activate"] = False

            minutes_difference = (datetime.now() - user["time"]).total_seconds() / 60
            print(minutes_difference)
            if minutes_difference >= 5:
                return {"message": f"time expired ,over {minutes_difference} minutes"}
            user_db.create_item(user)
            return {"message": "success", "data": user}
        except Exception as e:
            return {"message": str(e)}
    return {"message": "error"}


@admin.route("/")
@login_required
def a():
    if current_user.usertype != "admin":
        return redirect(url_for("views.home"))
    print(current_user)
    return render_template("admin.html")


@admin.route("/qrcode")
@login_required
def aqrcode():
    if current_user.usertype != "admin":
        return redirect(url_for("views.home"))
    return render_template("admin-qrcode.html")
