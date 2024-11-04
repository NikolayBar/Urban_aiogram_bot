from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

with open('UrbanStudentBot.token', 'r', encoding='utf-8') as f:
    api = f.read().strip()

bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'])
async def start(message):
    _msg = f'Привет! Я бот помогающий твоему здоровью.'
    print(message)
    await message.answer(_msg)


@dp.message_handler()
async def all_message(message):
    _msg = 'Введите команду /start, чтобы начать общение.'
    print(message)
    await message.answer(_msg)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
