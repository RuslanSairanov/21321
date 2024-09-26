from aiogram import types, Dispatcher, Bot
from aiogram.utils import executor
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from credits import token
import random
from aiogram.types import InlineKeyboardButton
from aiogram.utils import InlineKeyboardMarkup
menu = InlineKeyboardMarkup(row_width=2)
menu.add(
   InlineKeyboardButton("Проверить батарею", callback_data="check_battery"),
   InlineKeyboardButton("Проверить температуру", callback_data="check_temp"),
   InlineKeyboardButton("Начать уборку", callback_data="start_cleaning"),
   InlineKeyboardButton("Рассказать шутку", callback_data="tell_joke")
)


@dp.message(Command("menu"))
async def show_menu(message: Message):
   await message.answer("Выберите действие для EasyCoder:", reply_markup=menu)