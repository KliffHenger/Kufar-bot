from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage



TOKEN_API = "6173785703:AAGcYoU9lVs5XHmD566aJBO_HDLtuN6j8Yo" # токен Kufar_bot (@KufarForIlyaBot)


bot = Bot(TOKEN_API)
dp = Dispatcher(bot, storage=MemoryStorage())