from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup
from models import Homework



def get_student_menu() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(text="📚 Домашка", callback_data="menu_homework")
    builder.button(text="🎁Файлик по PYTHON только для своих", callback_data="free_python")
    builder.button(text="💬 Поддержка/Автор", callback_data="meee")
    builder.button(text="✅ Задачки", callback_data="menu_tasks")


    builder.adjust(1,2,1)
    return builder.as_markup()

def get_admin_menu() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(text="➕ Добавить ДЗ", callback_data="admin_add_homework")
    builder.button(text="✅ Проверка ДЗ", callback_data="admin_check_homework")
    builder.adjust(1)
    return builder.as_markup()

def get_guest_menu()-> InlineKeyboardMarkup:
    builder=InlineKeyboardBuilder()
    builder.button(text="🎁 Бесплатный файлик по Python", callback_data="free_python")
    builder.button(text="📢 Канал", callback_data="guest_channel")
    builder.button(text="💬 Автор", callback_data="meee")
    builder.button(text="📺 Урок", callback_data="guest_lesson")
    builder.button(text="✅ Задачки", callback_data="menu_tasks")
    builder.adjust(1,2,2)
    return builder.as_markup()


def get_homework_list_menu(homeworks: list[Homework]) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    for hw in homeworks:
        builder.button(text=hw.title, callback_data=f"hw_{hw.id}")
    builder.adjust(1)
    return builder.as_markup()

