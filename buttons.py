from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove




start = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(
    KeyboardButton('/start'),
    KeyboardButton('/car'),
    KeyboardButton('/quiz'),
    KeyboardButton('/reply_webapp'),
    KeyboardButton('/inline_webapp'),
    KeyboardButton('/registration'),
    KeyboardButton('/store')
    )


submit = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True).add(KeyboardButton('да'), KeyboardButton('нет'))
size = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3, one_time_keyboard=True).add(KeyboardButton('XS'),KeyboardButton('S'),KeyboardButton('M'),KeyboardButton('L'),KeyboardButton('XL'),KeyboardButton('XXL'),)
# Удаление кнопок из интерфейса
remove_keyboard = ReplyKeyboardRemove()