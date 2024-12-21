from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_user, login_required, logout_user
from .models import User, user_db
from werkzeug.security import check_password_hash


auth = Blueprint("auth", __name__)


@auth.route("/login")
def login():
    return render_template("login.html")


@auth.route("/login/api", methods=["POST"])
def loginapi():
    if request.method == "POST":
        sid = request.form.get("sid").lower()
        password = request.form.get("password")
        rememberme = request.form.get("rememberme") == "true"  # 確保布林值格式
        print(sid, password, rememberme)

        if not sid or not password:
            return {"message": "no input"}, 400  # 錯誤狀態碼

        # 從資料庫檢查用戶
        user = user_db.check_item(sid)
        if not user:
            return {"message": "sid does not exist"}, 404

        # 驗證密碼
        if "password" in user and check_password_hash(user["password"], password):
            login_user(
                User(user["_id"], user["name"], user["type"]), remember=rememberme
            )
            return {"message": "success"}, 200
        else:
            return {"message": "wrong password"}, 401
    return {"message": "error"}, 405  # 方法不允許


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("views.home"))
