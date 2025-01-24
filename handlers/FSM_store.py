from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from db import main_db
import buttons


class FSM_store(StatesGroup):
    name_product = State()
    size = State()
    category = State()
    price = State()
    collection = State()
    photo = State()
    product_id = State()
    info_product = State()
    submit = State()


async def start_fsm_store(message: types.Message):
    await message.answer('Введите название товара:', reply_markup=buttons.cancel)
    await FSM_store.name_product.set()


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name_product'] = message.text

    await FSM_store.next()
    await message.answer('Введите размер:')


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


async def product_id(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['product_id'] = message.text

    await FSM_store.next()
    await message.answer('информация о продукте')


async def info_product(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['info_product'] = message.text

    await FSM_store.next()
    await message.answer('Верные ли данные ?')
    await message.answer_photo(photo=data['photo'],
                               caption=f'Название товара - {data["name_product"]}\n'
                                       f'Размер товара - {data["size"]}\n'
                                       f'Категория - {data["category"]}\n'
                                       f'Артикул - {data["product_id"]}\n'
                                       f'Инфо - {data["info_product"]}\n'
                                       f'Цена - {data["price"]}')


async def submit_load(message: types.Message, state: FSMContext):
    if message.text == 'да':
        async with state.proxy() as data:
            await main_db.sql_insert_store(
                name_product=data['name_product'],
                size=data['size'],
                price=data['price'],
                photo=data['photo'],
                product_id=data['product_id']
            )
            await main_db.sql_insert_products_details(
                product_id=data['product_id'],
                info_product=data['info_product'],
                category=data['category']
            )
            await main_db.sql_insert_collection(
                product_id=data['product_id'],
                collection=data['collection']
            )
        await message.answer('Ваши данные в базе!', reply_markup=buttons.remove_keyboard)
    elif message.text == 'нет':
        await message.answer('Хорошо, отменено!', reply_markup=buttons.remove_keyboard)
        await state.finish()

    else:
        await message.answer('Выберите да или нет')


def register_handlers_fsm_store(dp: Dispatcher):
    dp.register_message_handler(start_fsm_store, commands='store')
    dp.register_message_handler(load_name, state=FSM_store.name_product)
    dp.register_message_handler(load_size, state=FSM_store.size)
    dp.register_message_handler(load_category, state=FSM_store.category)
    dp.register_message_handler(load_price, state=FSM_store.price)
    dp.register_message_handler(load_collection, state=FSM_store.collection)
    dp.register_message_handler(load_photo, state=FSM_store.photo, content_types=['photo'])
    dp.register_message_handler(info_product, state=FSM_store.info_product)
    dp.register_message_handler(product_id, state=FSM_store.product_id)
    dp.register_message_handler(submit_load, state=FSM_store.submit)
