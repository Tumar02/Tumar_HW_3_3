from aiogram import types, Dispatcher
from config import dp, bot


async def echo(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text=message.text)


def register_extra(dp: Dispatcher):
    dp.register_message_handler(echo)
