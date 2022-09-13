from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage


storage = MemoryStorage()
bot = Bot(token='5320585857:AAGp71Q5r4EPf6w9KfYc4YyXbMTnsDpzQ64')
dp = Dispatcher(bot, storage=storage)