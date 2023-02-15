from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Command
from airtable_config import table
from user_states import Search
from aiogram.dispatcher import FSMContext
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from config import bot, dp
from .parsing import urlify, get_url, get_price


async def start_bot(message: types.Message):
    all_table = table.all()
    is_user = False
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            is_user = True
            name_user = all_table[index]['fields']['UserName']
            await bot.send_message(message.from_user.id, text=f'Привет, {name_user}! Вы СТАРТ уже нажимали, можно начать отслеживание.\n\
Для этого введите команду /set_search , чтобы указать по какому слову (словосочетанию) бот будет отслеживать новые объявления.')
    if not is_user:
        table.create({'UserName': str(message.from_user.first_name),
                      'UserTGID': str(message.from_user.id),
                      'SearchWord': 'None',
                      'UrlProd': 'None',
                      'PriceProd': 'None',
                      'JobName': 'None'})
        await bot.send_message(message.from_user.id, text=f'Добро пожаловать в наш сервис!\n\
Введите команду /set_search , чтобы указать по какому слову (словосочетанию) бот будет отслеживать новые объявления.')

async def help_message(message: types.Message):
    await bot.send_message(message.from_user.id, 
                        text=f"Бот будет ходить на Куфар и искать новые обьявления по мере их появления.\n\n\
Команды бота:\n\
/start - ну понятно что делает.\n\
/help - инструкцию выдает.\n\
/set_search - тут мы вводим слова по которым бот будет следить.\n\
/go_search - это начинает отслеживание.\n\
/stop_search - останавливает отслеживание.")

async def set_search(message: types.Message):
    ''' тут мы на всякий случай останавливаем планировщик'''
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            try:
                job_name = all_table[index]['fields']['JobName']
                globals()[job_name].shutdown(wait=False) # отключение планировщика
            except:
                pass
    await bot.send_message(message.from_user.id, f"Введи название товара (напр. - стиральная машина) для отслеживания:")
    await Search.search_word.set()

async def input_word(message: types.Message, state=FSMContext):
    word = str(message.text)
    s_word = urlify(word)
    await state.update_data(search_word=message.text)
    all_table = table.all()   
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            element_id = all_table[index]['id']
            urla = get_url(s_word)
            table.update(record_id=str(element_id), fields={'UrlProd': str(urla)})
            table.update(record_id=str(element_id), fields={'SearchWord': str(s_word)})
            await bot.send_message(message.from_user.id, 
                    text=f'Вы ввели "{word}" и мы это сохранили.\nВведите команду /go_search , чтобы начать отслеживание.')
            await state.finish()
            
async def search_go(message: types.Message):
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
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
            for index in range(len(all_table)):
                if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
                    record_id = all_table[index]['id']

                    name_sched = 'sched'+str(message.from_user.id)
                    globals()[name_sched] = AsyncIOScheduler(timezone="Europe/Minsk")
                    
                    urla = str(get_url(s_word))
                    price = str(get_price(s_word))
                    table.update(record_id=str(record_id), fields={'UrlProd': urla})
                    table.update(record_id=str(record_id), fields={'PriceProd': price})
                    table.update(record_id=str(record_id), fields={'JobName': name_sched})
                    if price == 'None':
                        await bot.send_message(int(tg_id), text=f'По Вашему запросу "{s_word}" объявлений НЕ НАЙДЕНО.\n\n\
Используйте команду /set_search - чтобы изменить запрос.')
                    elif price != 'None':
                        await bot.send_message(int(tg_id), text=f'Первый найденый товар - {urla}\nЦена - {price}\nКогда появится еще, то придёт сообщение.')
                        print(name_sched)
                        mess_bd = {'tg_id': str(message.from_user.id), 'record_id': record_id}
                        print(mess_bd)
                        globals()[name_sched].add_job(send_message_prod, trigger='interval', minutes=1, 
                                                      kwargs={'mess_bd': mess_bd}, misfire_grace_time=3)
                        globals()[name_sched].start()
                        globals()[name_sched].print_jobs()



async def send_message_prod(mess_bd):
    tg_id = mess_bd['tg_id']
    record_id = mess_bd['record_id']
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(tg_id):
            old_url = all_table[index]['fields']['UrlProd']
            s_word = all_table[index]['fields']['SearchWord']
            new_url = str(get_url(s_word))
            print(new_url)
            for index in range(len(all_table)):
                if all_table[index]['fields']['UserTGID'] == str(tg_id) \
                    and all_table[index]['fields']['UrlProd'] != new_url:
                    record_id = all_table[index]['id']

                    urla = get_url(s_word)
                    price = get_price(s_word)

                    table.update(record_id=str(record_id), fields={'UrlProd': str(urla)})
                    table.update(record_id=str(record_id), fields={'PriceProd': str(price)})
                    await bot.send_message(int(tg_id), text=f'Ссылка на товар - {urla}\nЦена - {price}')
                else:
                    print('Новых товаров нет')


async def search_stop(message: types.Message):
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            try:
                job_name = all_table[index]['fields']['JobName']
                globals()[job_name].shutdown(wait=False) # отключение планировщика
                await bot.send_message(message.from_user.id, 
                    text=f'Отслеживание отключено.\n\nЧтобы возобновить отслеживание - введите команду /go_search\n\
Чтобы изменить запрос - введите /set_search')
            except:
                pass
            

async def message_for_all(message: types.Message):
    all_table = table.all()
    for index in range(len(all_table)):
        id_tg = all_table[index]['fields']['UserTGID']
        await bot.send_message(int(id_tg), text=f'Мы обновили нашего Бота.\n\
Из-за этого все активные отслеживания были остановленны.\n\n\
Для их перезапуска используйте команду /go_search')


def register_handlers_start(dp: Dispatcher):
    dp.register_message_handler(start_bot, Command('start'))
    dp.register_message_handler(help_message, Command('help'))
    dp.register_message_handler(set_search, Command('set_search'))
    dp.register_message_handler(input_word, state=Search.search_word)
    dp.register_message_handler(search_go, Command('go_search'))
    dp.register_message_handler(send_message_prod, commands=['40000_monkeys_put_a_banana_up_their_butt'])
    dp.register_message_handler(search_stop, Command('stop_search'))
    dp.register_message_handler(message_for_all, Command('1786314send_all_user'))
