from aiogram.types import ReplyKeyboardRemove, KeyboardButton, ReplyKeyboardMarkup

def get_keyboard(buttons):
    kb = []
    for button in buttons:
        kb.append([KeyboardButton(text=button)])
    reply_markup = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    return reply_markup