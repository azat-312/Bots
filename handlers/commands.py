from aiogram import Dispatcher, types, bot
import os
from config import bot
from random import sample



async def start_handler(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=f'Hello {message.from_user.first_name}!\n'
                                f'Твой telegram ID - {message.from_user.id}\n')

    await message.answer('Привет!')


# @db.message_handler(commands=['mem'])
async def mem_handler(message: types.Message):
    photo_path = os.path.join('media', 'images.jpeg')

    photo = open(photo_path, 'rb')

    await bot.send_photo(chat_id=message.from_user.id,
                             photo=photo,
                             caption='Это машина')


    #with open(photo_path, 'rb') as photo:
    #     await bot.send_photo(chat_id=message.from_user.id,
    #                          photo=photo,
    #                          caption='Это мем')
    #
    #     await message.answer_photo(photo=photo, caption='Мем')




dice_options = ['⚽', '🎰', '🏀', '🎯', '🎳', '🎲']

async def game_dice(message: types.Message):
    selected_dices = sample(dice_options, 3)
    selected_dice = sample(selected_dices, 1)[0]


    bot_message = await bot.send_dice(chat_id=message.chat.id, emoji=selected_dice)
    bot_score = bot_message.dice.value

    user_message = await bot.send_dice(chat_id=message.chat.id, emoji=selected_dice)
    user_score = user_message.dice.value


    if bot_score > user_score:
        await message.answer("вы проиграли")
    elif bot_score < user_score:
        await message.answer("Вы выиграли! ")
    else:
        await message.answer("Ничья!")



def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start'])
    dp.register_message_handler(mem_handler, commands=['car'])
    dp.register_message_handler(game_dice, commands=['game'])