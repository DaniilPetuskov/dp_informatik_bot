from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from crud import get_or_create_student
from config import ADMIN_ID
from keyboards import get_student_menu
from aiogram.filters import CommandStart, Command
from menu import show_main_menu
from aiogram import F
from aiogram.types import CallbackQuery
from crud import get_or_create_student,get_student_bedts,get_homework_by_id
from keyboards import get_homework_list_menu

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    student = get_or_create_student(
        telegram_id=message.from_user.id,
        name=message.from_user.full_name,
        username=message.from_user.username,
    )
    if message.from_user.id == int(ADMIN_ID):
        await message.answer("Здарова, пидармот")  # тут потом будет admin-клавиатура
    elif student.is_student:
        await message.answer(
            f"Привет, {student.name}! Твоя серия: {student.current_streak} 🔥")  # тут потом будет student-клавиатура
    else:
        await message.answer("Привет! Ты пока не помечен, как мой ученик, но я всё равно рад тебя видеть).")  # тут потом будет ограниченная клавиатура


@router.message(Command("menu"))
async def cmd_menu(message: Message):
    await show_main_menu(message)


@router.callback_query(F.data == "meee")
async def cmd_meee(callback: CallbackQuery):

    await callback.message.answer('1213')

@router.callback_query(F.data == "menu_homework")
async def show_homework_list(callback: CallbackQuery):
    student=get_or_create_student(
        telegram_id=callback.from_user.id,
        name=callback.from_user.full_name,
        username=callback.from_user.username,
    )
    debts=get_student_bedts(student.id)
    if not debts:

        await callback.message.answer("Долгов нет 🎉")

    else:

        await callback.message.answer(
            text="Твои домашечки: ",
            reply_markup=get_homework_list_menu(debts)
        )

    await callback.answer()


@router.callback_query(F.data.startswith("hw_"))
async def show_homework_detail(callback: CallbackQuery):
    homework_id = int(callback.data.split("_")[1])
    homework=get_homework_by_id(homework_id)
    if homework is None:
        await callback.message.answer("Домашка не найдена",show_alert=True)
        return

    text = f"📌 {homework.title}\n\n{homework.content}"
    await callback.message.answer(
        text=text,
        # reply_markup=get_homework_detail_menu(homework_id)
    )

    await callback.answer()