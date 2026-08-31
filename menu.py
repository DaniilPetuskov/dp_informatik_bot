from aiogram.filters import Command
from aiogram.types import Message
from config import ADMIN_ID
from crud import get_or_create_student
from keyboards import get_student_menu, get_admin_menu, get_guest_menu
from aiogram.types import FSInputFile


async def show_main_menu(message: Message):

    student = get_or_create_student(
        telegram_id=message.from_user.id,
        name=message.from_user.full_name,
        username=message.from_user.username,
    )

    if message.from_user.id == int(ADMIN_ID):

        await message.answer_photo(
            photo=FSInputFile('data/Logo_dp_informatik_prob_Version777.png'),
            caption="Админ-меню:",
            reply_markup=get_admin_menu(),
        )

    elif student.is_student:

        await message.answer_photo(
            photo=FSInputFile('data/Logo_dp_informatik_prob_Version777.png'),
            caption="Твоя серия: {student.current_streak} 🔥",
            reply_markup=get_student_menu()
        )

    else:
        await message.answer_photo(photo=FSInputFile('data/Logo_dp_informatik_prob_Version777.png'),
                                   text="Меню:",
                                   reply_markup=get_guest_menu())


