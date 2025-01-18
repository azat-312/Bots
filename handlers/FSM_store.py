from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
import buttons
from db import main_db

class FSM_store(StatesGroup):
    name = State()
    size = State()
    category = State()
    price = State()
    photo = State()
    productid = State()
    infoproduct = State()
    submit = State()


async def start_fsm_store(message: types.Message):
    await FSM_store.name.set()
    await message.answer('Напишите название товара:')


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text

    await FSM_store.next()
    await message.answer('Выберете размер товара:', reply_markup=buttons.size)


async def load_size(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['size'] = message.text

    await FSM_store.next()
    await message.answer('категория')


async def load_category(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['category'] = message.text

    await FSM_store.next()
    await message.answer('стоимость товара')


async def load_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = message.text

    await FSM_store.next()
    await message.answer('Отправьте  фотографию товара')


async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[-1].file_id

    await FSM_store.next()
    await message.answer('пропишите id продукта')

async def productid(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['productid'] = message.text

    await FSM_store.next()
    await message.answer('информация о продукте')

async def infoproduct(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['infoproduct'] = message.text
    await FSM_store.next()
    await message.answer('Верные ли данные ?')
    await message.answer_photo(photo=data['photo'],
                                   caption=f'название - {data["name"]}\n'
                                    f'размер - {data["size"]}\n'
                                    f'категория - {data["category"]}\n'
                                    f'стоимость  - {data["price"]}\n'
                                    f'id продукта - {data["productid"]}\n'
                                    f'информация о продукте -{data["infoproduct"]}\n',reply_markup=buttons.submit)

async def submit(message: types.Message, state: FSMContext):
    if message.text == 'да':

        async with state.proxy() as data:
            await main_db.sql_store_registered(
                name=data['name'],
                size=data['size'],
                category=data['category'],
                price=data['price'],
                photo=data['photo']
            )
        async with state.proxy() as data:
            await main_db.sql_products_details(
                category=data['category'],
                productid=data['productid'],
                infoproduct=data['infoproduct']
                )
            await message.answer('Ваши данные в базе', reply_markup=buttons.remove_keyboard)

        await state.finish()


    elif message.text == 'нет':
        await message.answer('Хорошо, отменено!', reply_markup=buttons.remove_keyboard)
        await state.finish()

    else:
        await message.answer('Выберите да или нет')


async def cancel_fsm(message: types.Message, state: FSMContext):
    current_state = await state.get_state()

    if current_state is not None:
        await state.finish()
        await message.answer('Отменено!', reply_markup=buttons.remove_keyboard)



def register_handlers_fsm_store(dp: Dispatcher):
    dp.register_message_handler(cancel_fsm, Text(equals='отмена', ignore_case=True), state='*')
    dp.register_message_handler(start_fsm_store, commands='store')
    dp.register_message_handler(load_name, state=FSM_store.name)
    dp.register_message_handler(load_size, state=FSM_store.size)
    dp.register_message_handler(load_category, state=FSM_store.category)
    dp.register_message_handler(load_price, state=FSM_store.price)
    dp.register_message_handler(load_photo, state=FSM_store.photo, content_types=['photo'])
    dp.register_message_handler(infoproduct,state=FSM_store.infoproduct)
    dp.register_message_handler(productid,state=FSM_store.productid)
    dp.register_message_handler(submit, state=FSM_store.submit)