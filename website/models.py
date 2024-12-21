import os
from dotenv import load_dotenv
from flask_login import UserMixin
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# 載入 .env 檔案
load_dotenv()

# 取得 MongoDB URI
MONGODB_URI = os.getenv("MONGODB_URI")
DB_NAME = "lib"  # 全局設置資料庫名稱


class User(UserMixin):
    """
    User 類別，定義用戶的基本屬性和方法
    """

    def __init__(self, user_id, username, usertype):
        self.id = user_id  # 用戶 ID
        self.username = username
        self.usertype = usertype

    def get_user(self):
        """
        返回用戶基本信息的字典格式
        """
        return {"_id": self.id, "name": self.username, "type": self.usertype}


class MongoServer:
    """
    MongoServer 類別，用於操作指定的 MongoDB 集合
    """

    def __init__(self, collection_name):
        try:
            # 連接 MongoDB 客戶端
            client = MongoClient(MONGODB_URI, server_api=ServerApi("1"))
            client.admin.command("ping")  # 測試連接是否成功
            print("Successfully connected to MongoDB!")
            # 設定資料庫與集合
            db = client[DB_NAME]
            self.collection = db[collection_name]
        except Exception as e:
            raise ConnectionError(f"Failed to connect to MongoDB: {e}")

    def check_item(self, item_id: str):
        """
        檢查集合中是否存在指定 ID 的文檔
        """
        return self.collection.find_one({"_id": item_id})

    def create_item(self, item: dict):
        """
        插入或替換一筆文檔
        """
        try:
            self.collection.insert_one(item)
            return "success"
        except Exception as e:
            # 如果插入失敗，替換已存在的文檔
            self.collection.replace_one({"_id": item["_id"]}, item, upsert=True)
            return f"replaced existing item: {e}"

    def create_new_item(self, item: dict):
        """
        創建新的文檔，如果已存在則返回對應提示
        """
        if self.check_item(item["_id"]):
            return "item already exists"
        return self.create_item(item)

    def find_all(self):
        """
        查詢集合中的所有文檔，返回為列表格式
        """
        try:
            return list(self.collection.find())
        except Exception as e:
            raise RuntimeError(f"Failed to retrieve items: {e}")

    def delete_item(self, item_id: str):
        """
        刪除集合中指定 ID 的文檔
        """
        try:
            result = self.collection.delete_one({"_id": item_id})
            if result.deleted_count > 0:
                print(f"Item with id: {item_id} successfully deleted.")
                return "success"
            else:
                print(f"Item with id: {item_id} not found.")
                return "item not found"
        except Exception as e:
            return f"Failed to delete item: {e}"


# 初始化用戶和圖書的 MongoServer 實例
user_db = MongoServer("user")
book_db = MongoServer("books")
