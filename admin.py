import random
from aiogram import types, Dispatcher


async def game(message: types.Message):
    emoji_list = ('⚽️', '🏀', '🎲', '🎯', '🎳', '🎰')
    emoji = random.choice(emoji_list)
    if message.text.startswith('game'):
        await message.answer_dice(emoji=emoji)


def register_admin(dp: Dispatcher):
    dp.register_message_handler(game)
