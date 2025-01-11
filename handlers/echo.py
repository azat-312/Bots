from aiogram import Dispatcher,  types
#dp.message_handler()
async def echo_handler(message: types.Message):
    if message.text.isdigit():
        await message.answer(int(message.text)**2)
    else:
        await message.answer(message.text)






def register_handlers(dp: Dispatcher):

    dp.register_message_handler(echo_handler)