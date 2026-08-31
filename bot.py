import asyncio
from db import create_db_and_tables
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from config import BOT_TOKEN
from handlers import main_router


dp = Dispatcher()
bot = Bot(token=BOT_TOKEN)
dp.include_router(main_router)

async def main():
    create_db_and_tables()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())