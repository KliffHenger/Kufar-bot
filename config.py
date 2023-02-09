from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage



TOKEN_API = "5801124476:AAGPSljD9fxksGJINgGmyAA9lwfW5kKn7xk" # токен all_test_bot (@my86352_bot)


bot = Bot(TOKEN_API)
dp = Dispatcher(bot, storage=MemoryStorage())