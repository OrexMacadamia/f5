import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command, CommandStart
from keyboard import *
from tok import *
from aiogram.fsm.storage.memory import MemoryStorage

storage = MemoryStorage()

bot = Bot(TOKEN)
dp = Dispatcher(storage=storage)


@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Привет я F5 бот")
    kb = [
        [types.KeyboardButton(text="Да")],
        [types.KeyboardButton(text="Нет")],
        [types.KeyboardButton(text="/52")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("Хотите начать новый спор?", reply_markup=keyboard)

@dp.message(Command("52"))
async def fivetwo(message: types.Message):
    await message.answer("В КОМПЫЫЫ!!!")

@dp.message(Command("dice"))
async def cmd_dice(message: types.Message):
    await message.answer_dice(emoji="🎲")


async def main():
    await dp.start_polling(bot)



if __name__ == "__main__":
    import logging
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())

