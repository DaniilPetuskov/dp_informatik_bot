from sqlmodel import SQLModel, create_engine,Session
from models import Student, Homework
DATABASE_URL='sqlite:///bot.db'
engine = create_engine(DATABASE_URL)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)