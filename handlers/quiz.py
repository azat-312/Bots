
# quiz.py
from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import bot


async def quiz_1(message: types.Message):
    keyboard = InlineKeyboardMarkup(resize_keyboard=True)

    button = InlineKeyboardButton('Далее', callback_data='button1')

    keyboard.add(button)

    question = 'pagani or bugatti'

    answer = ['pagani', 'bugatti', 'Оба']

    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation='Жаль...',
        open_period=60,
        reply_markup=keyboard
    )


async def quiz_2(call: types.CallbackQuery):
    question = 'dota2 or CS.GO'
    answer =['dota2','CS.GO']

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=True,
        type='quiz',
        correct_option_id=1,
        explanation='эх ты  . ..  .',
        open_period=30
    )
def register_handlers(dp: Dispatcher):
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_callback_query_handler(quiz_2,text='button1')