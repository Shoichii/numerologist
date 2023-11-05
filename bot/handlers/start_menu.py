from bot.loader import dp
from aiogram import types

@dp.message_handler(commands=['start'])
async def start_menu(msg: types.Message):
    await msg.answer('test')