from sqlmodel import Session, select
from db import engine
from models import Student,Homework

def get_or_create_student(telegram_id: int, name: str, username: str | None) -> Student:
    with Session(engine) as session:
        statement = select(Student).where(Student.telegram_id == telegram_id)
        student = session.exec(statement).first()

        if student is None:
            student = Student(
                telegram_id=telegram_id,
                tg_username=username,
                name=name,
            )
            session.add(student)
            session.commit()
            session.refresh(student)

        return student


def get_student_bedts(student_id:int) -> list[Homework]:
    with Session(engine) as session:
        statement = select(Homework).where(
            Homework.student_id == student_id,
            Homework.is_done == False,
        )
        return list(session.exec(statement).all())


def get_homework_by_id(homework_id:int) -> Homework | None:
    with Session(engine) as session:
        return session.get(Homework, homework_id)
