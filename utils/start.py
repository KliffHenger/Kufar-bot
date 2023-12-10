from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Command
from airtable_config import table
from user_states import Search
from aiogram.dispatcher import FSMContext
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from config import bot, dp
from .parsing import urlify, get_item
from keyboards.inline_menu import START, MENU, GO, STOP, ALL_MENU, REGION
from aiogram.utils.markdown import hlink
from datetime import datetime


async def start_bot(message: types.Message):
    all_table = table.all()
    is_user = False
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            is_user = True
            name_user = all_table[index]['fields']['UserName']
            await bot.send_message(message.from_user.id, text=f'Привет, {name_user}! Можно начинать отслеживание.\n\
Для помощи введите команду /help', reply_markup=START)
    if not is_user:
        await bot.send_message(message.from_user.id, text=f'Добро пожаловать в наш сервис!\n\
Введите команду /help для вывода описания функций или используйте кнопки под этим меню.', reply_markup=START)
        table.create({'UserName': str(message.from_user.first_name),
                      'UserTGID': str(message.from_user.id),
                      'DayLife': '2',
                      'SearchWord': 'None',
                      'Region': 'l',
                      'UrlProd': 'None',
                      'PriceProd': 'None',
                      'JobName': 'None'})

async def help_message(message: types.Message):
    await bot.send_message(message.from_user.id, 
                        text=f"Бот отслеживает новые обьявления от частных лиц на площадке Куфар и будет сообщать Вам по мере их появления.\n\
(Бесплатное время работы - 2 дня)\n\n\
По всем вопросам, оплаты и предложениям можете обращаться: {hlink ('Автор Бота', 'https://t.me/NikolayMiracle')} ", parse_mode='HTML', reply_markup=MENU)


@dp.callback_query_handler(text='set_word')
async def set_search(message: types.Message):
    ''' тут мы на всякий случай останавливаем планировщик'''
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id)\
                and all_table[index]['fields']['DayLife'] != '0':
            try:
                job_name = all_table[index]['fields']['JobName']
                # record_id = all_table[index]['id']
                globals()[job_name].shutdown(wait=False) # отключение планировщика
                # table.update(record_id=str(record_id), fields={'JobName': 'None'})
            except:
                pass
            await bot.send_message(message.from_user.id, f"Введи название товара (напр. - стиральная машина) для отслеживания:")
            await Search.search_word.set()
        elif all_table[index]['fields']['UserTGID'] == str(message.from_user.id)\
                and all_table[index]['fields']['DayLife'] == '0':
            try:
                job_name = all_table[index]['fields']['JobName']
                # record_id = all_table[index]['id']
                globals()[job_name].shutdown(wait=False) # отключение планировщика
                # table.update(record_id=str(record_id), fields={'JobName': 'None'})
            except:
                pass
            await bot.send_message(message.from_user.id, text=f'Дальнейшее использование нашего сервиса возможно только после уплаты \
абонентской платы в размере - 20 BYN (за 30 дней).\n\
Для уплаты необходимо связаться с автором, перейдя в пункт меню /help', reply_markup=MENU)
        


async def input_word(message: types.Message, state=FSMContext):
    word = str(message.text)
    s_word = urlify(word)
    await state.update_data(search_word=message.text)
    all_table = table.all()   
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            element_id = all_table[index]['id']
            reg = all_table[index]['fields']['Region']
            item = get_item(reg, s_word)
            print(item)
            try:
                urla = str(item[0])
                table.update(record_id=str(element_id), fields={'UrlProd': str(urla)})
                table.update(record_id=str(element_id), fields={'SearchWord': str(s_word)})
                await bot.send_message(message.from_user.id, 
                        text=f'Вы ввели "{word}" и мы это сохранили.', reply_markup=REGION)
                await state.finish()
            except:
                await bot.send_message(message.from_user.id, text=f'По Вашему запросу "{s_word}" объявлений НЕ НАЙДЕНО.\n\n\
Измените запрос.', reply_markup=START)
                await state.finish()

@dp.callback_query_handler(text='start_search')
async def search_go(message: types.Message):
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id)\
                and all_table[index]['fields']['DayLife'] != '0':
            try:
                job_name = all_table[index]['fields']['JobName']
                globals()[job_name].shutdown(wait=False) # отключение планировщика
            except:
                pass
            global record_id
            global tg_id
            tg_id, record_id = '', ''
            tg_id = str(message.from_user.id)
            for index in range(len(all_table)):
                if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
                    old_url = all_table[index]['fields']['UrlProd']
                    s_word = all_table[index]['fields']['SearchWord']
                    reg = all_table[index]['fields']['Region']
                    for index in range(len(all_table)):
                        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
                            record_id = all_table[index]['id']
                            name_sched = 'sched'+str(message.from_user.id)
                            globals()[name_sched] = AsyncIOScheduler(timezone="Europe/Minsk")
                            item = get_item(reg, s_word)
                            try:
                                urla = str(item[0])
                                price = str(item[1])
                                img = str(item[2])
                                
                                table.update(record_id=str(record_id), fields={'UrlProd': urla})
                                table.update(record_id=str(record_id), fields={'PriceProd': price})
                                table.update(record_id=str(record_id), fields={'JobName': name_sched})
                                msg_text=f"Первый найденый товар - {urla}\nЦена - {price}\n\
Когда появится еще, то сообщение придёт автоматически."
                                await bot.send_photo(int(tg_id), photo=img, caption=msg_text, reply_markup=STOP, parse_mode='HTML')
                                print(name_sched)
                                mess_bd = {'tg_id': str(message.from_user.id), 'record_id': record_id}
                                print(mess_bd)
                                # globals()[name_sched].add_job(send_message_prod, trigger='interval', seconds=5, # строчка для тестов
                                                            # kwargs={'mess_bd': mess_bd}, misfire_grace_time=10)
                                globals()[name_sched].add_job(send_message_prod, trigger='interval', minutes=1, # рабочая строчка (интервал больше будет пропускать  некоторые новые обьявления между опровами (проблема IPHONE в Минске))
                                                            kwargs={'mess_bd': mess_bd}, misfire_grace_time=10)
                                globals()[name_sched].start()
                                globals()[name_sched].print_jobs()
                            except:
                                await bot.send_message(int(tg_id), text=f'По Вашему запросу "{s_word}" объявлений НЕ НАЙДЕНО.\n\n\
Измените запрос.', reply_markup=START)
        elif all_table[index]['fields']['UserTGID'] == str(message.from_user.id)\
                and all_table[index]['fields']['DayLife'] == '0':
            try:
                job_name = all_table[index]['fields']['JobName']
                globals()[job_name].shutdown(wait=False) # отключение планировщика
            except:
                pass
            await bot.send_message(message.from_user.id, text=f'Дальнейшее использование нашего сервиса возможно только после уплаты \
абонентской платы в размере - СКОЛЬКО СЧИТАЕТЕ НУЖНЫМ (за 30 дней).\n\
Для уплаты необходимо связаться с автором, перейдя в пункт меню /help', reply_markup=MENU)


async def send_message_prod(mess_bd):
    tg_id = mess_bd['tg_id']
    record_id = mess_bd['record_id']
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(tg_id):
            old_url = all_table[index]['fields']['UrlProd']
            s_word = all_table[index]['fields']['SearchWord']
            reg = all_table[index]['fields']['Region']
            item = get_item(reg, s_word)
            print(item)
            new_url = str(item[0])
            for index in range(len(all_table)):
                if all_table[index]['fields']['UserTGID'] == str(tg_id) \
                    and all_table[index]['fields']['UrlProd'] != new_url:
                    record_id = all_table[index]['id']
                    item = get_item(reg, s_word)
                    urla = str(item[0])
                    price = str(item[1])
                    img = str(item[2])
                    table.update(record_id=str(record_id), fields={'UrlProd': str(urla)})
                    table.update(record_id=str(record_id), fields={'PriceProd': str(price)})
                    msg_text=f'Ссылка на товар - {urla}\nЦена - {price}'
                    await bot.send_photo(int(tg_id), photo=img, caption=msg_text, reply_markup=STOP, parse_mode='HTML')
                elif all_table[index]['fields']['UserTGID'] == str(tg_id) \
                    and all_table[index]['fields']['UrlProd'] == new_url:
                    print(f'{datetime.now()} Нет новых товаров для - {tg_id}')


# async def search_stop(message: types.Message):
#     all_table = table.all()
#     for index in range(len(all_table)):
#         if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
#             try:
#                 job_name = all_table[index]['fields']['JobName']
#                 globals()[job_name].shutdown(wait=False) # отключение планировщика
#                 await bot.send_message(message.from_user.id, 
#                     text=f'Отслеживание отключено.', reply_markup=MENU)
#             except:
#                 pass
        
@dp.callback_query_handler(text='stop_search')
async def search_stop(message: types.Message):
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            try:
                job_name = all_table[index]['fields']['JobName']
                # record_id = all_table[index]['id']
                globals()[job_name].shutdown(wait=False) # отключение планировщика
                await bot.send_message(message.from_user.id, 
                    text=f'Отслеживание отключено.', reply_markup=MENU)
                # table.update(record_id=str(record_id), fields={'JobName': 'None'})
            except:
                pass
            

async def message_for_all(message: types.Message):
    all_table = table.all()
    for index in range(len(all_table)):
        id_tg = all_table[index]['fields']['UserTGID']
        try:
#             await bot.send_message(int(id_tg), text=f'Извините за беспокойство.\n\
# Мы активно работаем над улучшениями и привлечением новых пользователей, поэтому переезжаем на другой адрес - @BestPriceKufarBot\n\
# Будем рады помогать вам в будущем.', reply_markup=MENU)
            await bot.send_message(int(id_tg), text=f'Здравствуйте.\n\
Мы активно работаем над улучшениями и новыми функциями.\n\
Из-за этого возможно активные отслеживания были остановленны.\n\n\
Для их перезапуска используйте соответствующие пункты меню.\n\
Так же, для увеличения точности отслеживания следует выбирать свой регион. (Со старта указывается "Вся Беларусь").\n\
Тепер не обязательно переходить по ссылке на товар, ведь фото товара - гораздо информативнее.\n\
Если у Вас есть предложения, то обязательно свяжитесь с нами.', reply_markup=MENU)
            print(id_tg+' - получил')
        except:
            pass

async def start_job_for_all(message: types.Message):
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['DayLife'] != '0' and all_table[index]['fields']['JobName'] != 'None':
            record_id = all_table[index]['id']
            name_sched = all_table[index]['fields']['JobName']
            tg_id = all_table[index]['fields']['UserTGID']
            mess_bd = {'tg_id': tg_id, 'record_id': record_id}
            globals()[name_sched] = AsyncIOScheduler(timezone="Europe/Minsk")
            # globals()[name_sched].add_job(send_message_prod, trigger='interval', seconds=5, # строчка для тестов
                                        # kwargs={'mess_bd': mess_bd}, misfire_grace_time=10)
            globals()[name_sched].add_job(send_message_prod, trigger='interval', minutes=1, # рабочая строчка
                                        kwargs={'mess_bd': mess_bd}, misfire_grace_time=10)
            globals()[name_sched].start()
            globals()[name_sched].print_jobs()
        

@dp.callback_query_handler(text='menu')
async def get_menu(message: types.Message):
    await bot.send_message(message.from_user.id, text=f'\U000026A1 Главное Меню \U000026A1', 
                           parse_mode='HTML', reply_markup=ALL_MENU)

async def get_menu(message: types.Message):
    await bot.send_message(message.from_user.id, text=f'\U000026A1 Главное Меню \U000026A1', 
                           parse_mode='HTML', reply_markup=ALL_MENU)

def register_handlers_start(dp: Dispatcher):
    dp.register_message_handler(start_bot, Command('start'))
    dp.register_message_handler(help_message, Command('help'))
    dp.register_message_handler(get_menu, Command('menu'))
    dp.register_message_handler(input_word, state=Search.search_word)
    dp.register_message_handler(send_message_prod, commands=['40000_monkeys_put_a_banana_up_their_butt'])
    dp.register_message_handler(start_job_for_all, Command('1786314start_job_for_all'))
    dp.register_message_handler(message_for_all, Command('1786314send_all_user'))
