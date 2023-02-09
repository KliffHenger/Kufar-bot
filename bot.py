from config import dp
from aiogram.utils import executor
from utils import start


async def on_startup(_):
    print('Ilya! Everything started, but that does not mean anything.')
 

"""Регистрация всех месадж-хэндлеров"""
start.register_handlers_start(dp)





if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)