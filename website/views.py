from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user
import random, string
from datetime import datetime
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from .models import user_db, book_db


views = Blueprint("views", __name__)

