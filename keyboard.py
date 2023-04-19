from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

mark_up = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    row_width=4
)

start_button = KeyboardButton("/start")
quiz_button = KeyboardButton("/quiz")
game_button = KeyboardButton("/game")
mentor_button = KeyboardButton("/mentor")
pin_button = KeyboardButton("/pin")

share_contact = KeyboardButton("Share contact", request_contact=True)
share_location = KeyboardButton("Share location", request_location=True)

mark_up.add(
    start_button, quiz_button, game_button, mentor_button, pin_button, share_location, share_contact
)

cancel_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    row_width=4
).add(
    KeyboardButton("Cancel")
)

confirm_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    row_width=3
).add(
    KeyboardButton("Yes"),
    KeyboardButton("Again"),
    KeyboardButton("Cancel")
)
