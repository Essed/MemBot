from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

queue_keyboard = InlineKeyboardMarkup(row_width = 2)

accept_button = InlineKeyboardButton(text = "Принять", callback_data = "Принять")
reject_button = InlineKeyboardButton(text = "Отклонить", callback_data = "Отклонить")

queue_keyboard.add(accept_button, reject_button)