from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
# from pymongo.errors import ConnectionError


def get_db():
    mongodb_url = "mongodb+srv://hwnam:1234@keyword.w3p74.mongodb.net/?retryWrites=true&w=majority&appName=Keyword"
    try:
        client = MongoClient(mongodb_url, tls=True)
        # 데이터베이스 연결 확인을 위해 간단한 쿼리 실행
        db = client["keyword"]
        # 컬렉션 목록을 가져와서 출력
        collections = db.list_collection_names()
        print("연결 성공:", collections)
        return db
    except ConnectionError as e:
        print("연결 실패:", e)
        return None