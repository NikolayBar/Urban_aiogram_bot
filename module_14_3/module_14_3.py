from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher import FSMContext
import asyncio


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


with open('UrbanStudentBot.token', 'r', encoding='utf-8') as f:
    api = f.read().strip()

bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

button_1 = KeyboardButton(text='Рассчитать')
button_2 = KeyboardButton(text='Информация')
button_3 = KeyboardButton(text='Купить')
kb = ReplyKeyboardMarkup(keyboard=[[button_1, button_2], [button_3]], resize_keyboard=True)

i_button_1 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
i_button_2 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
i_kb = InlineKeyboardMarkup(inline_keyboard=[[i_button_1, i_button_2]])

i_button_3 = InlineKeyboardButton('Product1', callback_data='product_buying')
i_button_4 = InlineKeyboardButton('Product2', callback_data='product_buying')
i_button_5 = InlineKeyboardButton('Product3', callback_data='product_buying')
i_button_6 = InlineKeyboardButton('Product4', callback_data='product_buying')
i_menu = InlineKeyboardMarkup(inline_keyboard=[[i_button_3,
                                                i_button_4,
                                                i_button_5,
                                                i_button_6]])


@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=i_kb)


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('10 х вес(кг) + 6,25 x рост(см) – 5 х возраст(г) + 5')
    await call.answer()


@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()
    await call.answer()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост (см):')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес (кг):')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    # для мужчин: 10 х вес(кг) + 6,25 x рост(см) – 5 х возраст(г) + 5;
    # для женщин: 10 x вес(кг) + 6,25 x рост(см) – 5 x возраст(г) – 161.
    a, g, w = data['age'], data['growth'], data['weight']
    res = eval(f'(10 * {w}) + (6.25 * {g}) - (5 * {a}) + 5')
    await message.answer(f'Ваша норма калорий {res} в сутки')
    await state.finish()


@dp.message_handler(commands=['start'])
async def start(message):
    _msg = f'Привет! Я бот помогающий твоему здоровью.'
    await message.answer(_msg, reply_markup=kb)


@dp.message_handler(text='Купить')
async def get_buying_list(message):
    images = ['pic_1.jpg', 'pic_2.jpg', 'pic_3.jpg', 'pic_4.jpg']
    for i in range(4):
        with open(images[i], 'rb') as img:
            txt_msg = f'Название: Product{i + 1} | Описание: описание {i + 1} | Цена: {(i + 1) * 100}'
            await message.answer_photo(img, txt_msg)
    await message.answer('Выберите продукт для покупки:', reply_markup=i_menu)


@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()


@dp.message_handler()
async def all_message(message):
    _msg = 'Введите команду /start, чтобы начать общение.'
    await message.answer(_msg)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)