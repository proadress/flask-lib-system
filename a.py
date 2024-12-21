import os
from dotenv import load_dotenv
from pymongo import MongoClient
from werkzeug.security import generate_password_hash

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")

# 更新 MongoDB 中用戶的密碼哈希
client = MongoClient(MONGODB_URI)
db = client["lib"]
user_collection = db["user"]

# 假設要更新用戶的密碼
sid = "0096c029"
password = "A131006220"
hashed_password = generate_password_hash(password)
user_collection.update_one({"_id": sid}, {"$set": {"password": hashed_password}})
