from aiogram import types,Bot, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from .import keyboard
from config import bot


ID = None


class FSMMentors(StatesGroup):
    id = State()
    name = State()
    direction = State()
    age = State()
    group = State()
    confirm = State()


async def admin(message: types.Message):
    global ID
    ID = message.from_user.id
    await bot.send_message(message.from_user.id, "Are you admin?")
    await message.delete()


async def start_list(message: types.Message):
    if message.from_user.id == ID:
        if message.chat.type == "private":
            await FSMMentors.id.set()
            await message.answer('ID')
        else:
            await message.answer("This chat should be private")


async def load_id(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as i:
            i['ID'] = message.text
        await FSMMentors.next()
        await message.answer("Name of mentor?", reply_markup=keyboard.confirm_markup)


async def load_name(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as i:
            i['name'] = message.text
        await FSMMentors.next()
        await message.answer("Direction of mentor?", reply_markup=keyboard.confirm_markup)


async def load_dir(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as i:
            i["direction"] = message.text
        await FSMMentors.next()
        await message.answer("Age of mentor?", reply_markup=keyboard.confirm_markup)


async def load_age(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        if not message.text.isdigit():
            await message.answer("It should be number!")
        else:
            async with state.proxy() as i:
                i["age"] = message.text
            await FSMMentors.next()
            await message.answer("Group?")


async def load_group(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as i:
            i["group"] = message.text
        await message.answer("Good!")
        await message.answer(
         f'{i["name"]} {i["direction"]} {i["age"]} {i["group"]}'
        )
        await message.answer("Are you sure?")


async def confirm_state(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        if message.text.capitalize() == "Yes":
            await state.finish()
        if message.text.capitalize() == "Again":
            await FSMMentors.name.set()
            await message.answer("Ok, restart!", reply_markup=keyboard.confirm_markup)


async def cancel_reg(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        current_state = await state.get_state()
        if current_state:
            await state.finish()


def register_mentors(dp: Dispatcher):
    dp.register_message_handler(admin, commands=['admin'], is_chat_admin=True)
    dp.register_message_handler(cancel_reg, state="*", commands=['cancel'])
    dp.register_message_handler(cancel_reg, Text(equals='cancel', ignore_case=True), state="*")
    dp.register_message_handler(register_mentors, commands=['mentor'], state=None)
    dp.register_message_handler(load_id, state=FSMMentors.id)
    dp.register_message_handler(load_name, state=FSMMentors.name)
    dp.register_message_handler(load_dir, state=FSMMentors.direction)
    dp.register_message_handler(load_age, state=FSMMentors.age)
    dp.register_message_handler(load_group, state=FSMMentors.group)
    dp.register_message_handler(confirm_state, state=FSMMentors.confirm)