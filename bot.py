from config import dp, bot
from aiogram.utils import executor
from utils import start
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from airtable_config import table
from keyboards.inline_menu import MENU


async def every_day():
    all_table = table.all()
    for index in range(len(all_table)):
        if int(all_table[index]['fields']['DayLife']) > 0:
            tg_id = all_table[index]['fields']['UserTGID']
            record_id = all_table[index]['id']
            quantity_day = int(all_table[index]['fields']['DayLife'])-1
            table.update(record_id=record_id, fields={'DayLife': str(quantity_day)})
            print(tg_id +' -1 день использования сервиса')
        elif int(all_table[index]['fields']['DayLife']) == 0:
            tg_id = all_table[index]['fields']['UserTGID']
            try:
                job_name = all_table[index]['fields']['JobName']
                record_id = all_table[index]['id']
                globals()[job_name].shutdown(wait=False) # отключение планировщика
                table.update(record_id=str(record_id), fields={'JobName': 'None'})
            except:
                pass
            try:
                await bot.send_message(int(tg_id), text=f'Дальнейшее использование нашего сервиса возможно только после уплаты \
абонентской платы в размере - 20 BYN за 30 дней (сумма не окончательна и обсуждению подлежит).\n\
Для уплаты или обсуждения суммы необходимо связаться с автором, перейдя в пункт меню /help', reply_markup=MENU)
            except:
                pass


async def on_startup(_):
    print('Everything started, but that does not mean anything.')
    sched = AsyncIOScheduler(timezone="Europe/Minsk")
    # sched.add_job(every_day, trigger='interval', minutes=1, misfire_grace_time=60) # строчка для тестов
    sched.add_job(every_day, trigger='interval', days=1, misfire_grace_time=60) # рабочая строчка
    sched.start()
    sched.print_jobs()
    



 

"""Регистрация всех месадж-хэндлеров"""
start.register_handlers_start(dp)





if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)