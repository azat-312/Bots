from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
import buttons
from aiogram.dispatcher.filters import Text
from db import main_db

class FSM_store(StatesGroup):
    name = State()
    size = State()
    category = State()
    price = State()
    collection = State()
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
    await message.answer('какая коллекция')


async def load_collection(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['collection'] = message.text

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
                                    f'информация о продукте -{data["infoproduct"]}\n'
                                    f'коллекция продукта - {data["collection"]}\n',reply_markup=buttons.submit)

async def submit(message: types.Message, state: FSMContext):
    if message.text == 'да':
        async with state.proxy() as data:
            await main_db.sql_insert_store(
                name=data['name'],
                size=data['size'],
                category=data['category'],
                price=data['price'],
                photo=data['photo']
            )
            await main_db.sql_insert_products_details(
                productid=data['productsid'],
                infoproduct=data['infoproduct'],
                category=data['category_product']
            )
            await main_db.sql_insert_collection(
                productid=data['productsid'],
                collection=data['collection']
            )
        await message.answer('Ваши данные в базе!', reply_markup=buttons.remove_keyboard)
        await state.finish()
    elif message.text == 'нет':
        await message.answer('Хорошо, отменено!', reply_markup=buttons.remove_keyboard)
        await state.finish()

    else:
        await message.answer('Выберите да или нет')
def register_handlers_fsm_store(dp: Dispatcher):
    dp.register_message_handler(start_fsm_store, commands='store')
    dp.register_message_handler(load_name, state=FSM_store.name)
    dp.register_message_handler(load_size, state=FSM_store.size)
    dp.register_message_handler(load_category, state=FSM_store.category)
    dp.register_message_handler(load_price, state=FSM_store.price)
    dp.register_message_handler(load_collection, state=FSM_store.collection)
    dp.register_message_handler(load_photo, state=FSM_store.photo, content_types=['photo'])
    dp.register_message_handler(infoproduct,state=FSM_store.infoproduct)
    dp.register_message_handler(productid,state=FSM_store.productid)
    dp.register_message_handler(submit, state=FSM_store.submit)