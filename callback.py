from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import dp, bot


# @dp.callback_query_handler(text="button_1")
async def start_quiz_1(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_2 = InlineKeyboardButton('NEXT', callback_data="button_2")
    markup.add(button_2)
    question = "Which of them is Korean food?"
    answer = [
        "Pizza",
        "Lagman",
        "Kimchi",
        "Pasta",
    ]
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type="quiz",
        correct_option_id=2,
        open_period=5,
        reply_markup=markup
    )


# @dp.callback_query_handler(text="button_2")
async def start_quiz_2(call: types.CallbackQuery):
    question = "The most popular K pop group"
    answer = [
        "BTS",
        "Blackpink"
        "EXO",
        "Twice",
    ]
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type="quiz",
        correct_option_id=0,
        open_period=5,
    )


async def send_message(message: types.Message):
    if message.reply_to_message:
        await message.pin()
    else:
        pass


def register_callback(dp: Dispatcher):
    dp.register_message_handler(start_quiz_1, text="button_1")
    dp.register_message_handler(start_quiz_2, text="button_2")
    dp.register_message_handler(send_message, commands=['!pin'])