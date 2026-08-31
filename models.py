from sqlmodel import SQLModel,Field
from typing import Optional
from datetime import date

class Student(SQLModel,table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    telegram_id: int = Field(unique=True, index=True)
    tg_username: Optional[str] = Field(default=None, unique=True, index=True)
    name: str
    is_student: bool = Field(default=False)
    current_streak: int = Field(default=0)
    max_streak: int = Field(default=0)
    freezes_available: int = Field(default=2)
    last_activity_date: Optional[date] = None


class Homework(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    student_id: int = Field(foreign_key="student.id")
    title: str
    content: str
    content_type: str  # "link" или "file"
    is_done: bool = Field(default=False)