from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

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

