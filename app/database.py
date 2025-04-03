# import time
# import psycopg2
# from psycopg2.extras import RealDictCursor

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

from .config import settings

# while True:
#     try:
#         conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='190394', cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Database connection was successful.")
#         break
#     except Exception as error:
#         print("Database connection failed")
#         print(error)
#         time.sleep(2)

# my_posts = [{"title" : "TITLE1", "content" : "CONTENT1", "id":1}, {"title" : "TITLE2", "content" : "CONTENT2", "id":2}]

SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()