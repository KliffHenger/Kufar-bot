from aiogram import types, Dispatcher
from airtable_config import table
from aiogram.dispatcher import FSMContext
from config import bot, dp
from keyboards.inline_regions import REGIONS, MINSK, BRESTSKAYA_OBL, VITEBSKAYA_OBL, GOMELSKAYA_OBL, \
                                        GRODNENSKAYA_OBL, MINSKAYA_OBL, MOGILEVSKAYA_OBL
from keyboards.inline_menu import GO


@dp.callback_query_handler(text='region_select')
async def region_select(message: types.Message):
    ''' тут мы на всякий случай останавливаем планировщик'''
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            try:
                job_name = all_table[index]['fields']['JobName']
                globals()[job_name].shutdown(wait=False) # отключение планировщика
            except:
                pass
    await bot.send_message(message.from_user.id, text=f"Выберите подходящий регион отслеживания:", reply_markup=REGIONS)

@dp.callback_query_handler(text='vsya_belarus')
async def vsya_belarus(message: types.Message):
    reg = 'l'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Всю Беларусь', reply_markup=GO)

@dp.callback_query_handler(text='ves_minsk')
async def ves_minsk(message: types.Message):
    await bot.send_message(message.from_user.id, text=f"Выберите подходящий район Минска или все для отслеживания:", 
                           reply_markup=MINSK)

@dp.callback_query_handler(text='minsk')
async def minsk(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'minsk'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Минск', reply_markup=GO)

@dp.callback_query_handler(text='minsk-centralnyj')
async def minsk_centralnyj(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'minsk-centralnyj'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Минск, Центральный р-н', reply_markup=GO)

@dp.callback_query_handler(text='minsk-sovetskij')
async def minsk_sovetskij(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'minsk-sovetskij'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Минск, Советский р-н', reply_markup=GO)

@dp.callback_query_handler(text='mins-pervomajskij')
async def mins_pervomajskij(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'mins-pervomajskij'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Минск, Первомайский р-н', reply_markup=GO)

@dp.callback_query_handler(text='minsk-partizanskij')
async def minsk_partizanskij(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'minsk-partizanskij'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Минск, Партизанский р-н', reply_markup=GO)

@dp.callback_query_handler(text='minsk-zavodskoj')
async def minsk_zavodskoj(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'minsk-zavodskoj'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Минск, Заводской р-н', reply_markup=GO)

@dp.callback_query_handler(text='minsk-leninskij')
async def minsk_leninskij(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'minsk-leninskij'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Минск, Ленинский р-н', reply_markup=GO)

@dp.callback_query_handler(text='minsk-oktyabrskij')
async def minsk_oktyabrskij(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'minsk-oktyabrskij'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Минск, Октябрьский р-н', reply_markup=GO)

@dp.callback_query_handler(text='minsk-moskovskij')
async def minsk_moskovskij(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'minsk-moskovskij'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Минск, Московский р-н', reply_markup=GO)

@dp.callback_query_handler(text='minsk-frunzenskij')
async def minsk_frunzenskij(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'minsk-frunzenskij'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Минск, Фрунзенский р-н', reply_markup=GO)

@dp.callback_query_handler(text='vsa_brestskaya')
async def vsa_brestskaya(message: types.Message):
    await bot.send_message(message.from_user.id, text=f"Выберите подходящий город Брестской обл. или все для отслеживания:", 
                           reply_markup=BRESTSKAYA_OBL)

@dp.callback_query_handler(text='brestskaya-obl')
async def brestskaya_obl(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'brestskaya-obl'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Всю Брестскую обл.', reply_markup=GO)

@dp.callback_query_handler(text='brest')
async def brest(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'brest'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Брест', reply_markup=GO)

@dp.callback_query_handler(text='baranovichi')
async def baranovichi(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'baranovichi'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Барановичи', reply_markup=GO)

@dp.callback_query_handler(text='bereza')
async def bereza(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'bereza'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Береза', reply_markup=GO)

@dp.callback_query_handler(text='beloozersk')
async def beloozersk(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'beloozersk'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Белоозерск', reply_markup=GO)

@dp.callback_query_handler(text='vysokae')
async def vysokae(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'vysokae'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Высокое', reply_markup=GO)

@dp.callback_query_handler(text='gancevichi')
async def gancevichi(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'gancevichi'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Ганцевичи', reply_markup=GO)

@dp.callback_query_handler(text='davyd-haradok')
async def davyd_haradok(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'davyd-haradok'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Давид-Городок', reply_markup=GO)

@dp.callback_query_handler(text='drogichin')
async def drogichin(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'drogichin'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Дрогичин', reply_markup=GO)

@dp.callback_query_handler(text='zhabinka')
async def zhabinka(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'zhabinka'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Жабинка', reply_markup=GO)

@dp.callback_query_handler(text='ivanovo')
async def ivanovo(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'ivanovo'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Иваново', reply_markup=GO)

@dp.callback_query_handler(text='ivacevichi')
async def ivacevichi(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'ivacevichi'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Ивацевичи', reply_markup=GO)

@dp.callback_query_handler(text='kamenec')
async def kamenec(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'kamenec'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Каменец', reply_markup=GO)

@dp.callback_query_handler(text='kobrin')
async def kobrin(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'kobrin'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Кобрин', reply_markup=GO)

@dp.callback_query_handler(text='luninec')
async def luninec(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'luninec'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Лунинец', reply_markup=GO)

@dp.callback_query_handler(text='lyahovichi')
async def lyahovichi(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'lyahovichi'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Ляховичи', reply_markup=GO)

@dp.callback_query_handler(text='malorita')
async def malorita(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'malorita'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Малорита', reply_markup=GO)

@dp.callback_query_handler(text='mikashevichy')
async def mikashevichy(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'mikashevichy'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Микашевичи', reply_markup=GO)

@dp.callback_query_handler(text='pinsk')
async def pinsk(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'pinsk'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Пинск', reply_markup=GO)

@dp.callback_query_handler(text='pruzhany')
async def pruzhany(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'pruzhany'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Пружаны', reply_markup=GO)

@dp.callback_query_handler(text='stolin')
async def stolin(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'stolin'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Столин', reply_markup=GO)

@dp.callback_query_handler(text='brestskaya-obl-drugie')
async def brestskaya_obl_drugie(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'brestskaya-obl-drugie'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Другие города', reply_markup=GO)

@dp.callback_query_handler(text='vsa_vitebslaya')
async def vsa_vitebslaya(message: types.Message):
    await bot.send_message(message.from_user.id, text=f"Выберите подходящий город Витебской обл. или все для отслеживания:", 
                           reply_markup=VITEBSKAYA_OBL)


@dp.callback_query_handler(text='vitebskaya-obl')
async def vitebskaya_obl(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'vitebskaya-obl'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Всю Витебскую обл.', reply_markup=GO)

@dp.callback_query_handler(text='vitebsk')
async def vitebsk(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'vitebsk'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Витебск', reply_markup=GO)

@dp.callback_query_handler(text='beshenkovichi')
async def beshenkovichi(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'beshenkovichi'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Бешенковичи', reply_markup=GO)

@dp.callback_query_handler(text='baran')
async def baran(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'baran'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Барань', reply_markup=GO)

@dp.callback_query_handler(text='braslav')
async def braslav(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'braslav'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Браслав', reply_markup=GO)

@dp.callback_query_handler(text='verhnedvinsk')
async def verhnedvinsk(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'verhnedvinsk'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Верхнедвинск', reply_markup=GO)

@dp.callback_query_handler(text='glubokoe')
async def glubokoe(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'glubokoe'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Глубокое', reply_markup=GO)

@dp.callback_query_handler(text='gorodok')
async def gorodok(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'gorodok'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Городок', reply_markup=GO)

@dp.callback_query_handler(text='dubrovno')
async def dubrovno(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'dubrovno'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Дубровно', reply_markup=GO)

@dp.callback_query_handler(text='lepel')
async def lepel(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'lepel'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Лепель', reply_markup=GO)

@dp.callback_query_handler(text='liozno')
async def liozno(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'liozno'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Лиозно', reply_markup=GO)

@dp.callback_query_handler(text='miory')
async def miory(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'miory'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Миоры', reply_markup=GO)

@dp.callback_query_handler(text='novolukoml')
async def novolukoml(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'novolukoml'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Новолукомль', reply_markup=GO)

@dp.callback_query_handler(text='novopolock')
async def novopolock(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'novopolock'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Новополоцк', reply_markup=GO)

@dp.callback_query_handler(text='orsha')
async def orsha(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'orsha'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Орша', reply_markup=GO)

@dp.callback_query_handler(text='polock')
async def polock(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'polock'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Полоцк', reply_markup=GO)

@dp.callback_query_handler(text='postavy')
async def postavy(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'postavy'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Поставы', reply_markup=GO)

@dp.callback_query_handler(text='rossony')
async def rossony(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'rossony'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Россоны', reply_markup=GO)

@dp.callback_query_handler(text='senno')
async def senno(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'senno'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Сенно', reply_markup=GO)

@dp.callback_query_handler(text='tolochin')
async def tolochin(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'tolochin'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Толочин', reply_markup=GO)

@dp.callback_query_handler(text='ushachi')
async def ushachi(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'ushachi'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Ушачи', reply_markup=GO)

@dp.callback_query_handler(text='chashniki')
async def chashniki(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'chashniki'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Чашники', reply_markup=GO)

@dp.callback_query_handler(text='sharkovshchina')
async def sharkovshchina(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'sharkovshchina'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Шарковщина', reply_markup=GO)

@dp.callback_query_handler(text='shumilino')
async def shumilino(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'shumilino'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Шумилино', reply_markup=GO)

@dp.callback_query_handler(text='vitebskaya-obl-drugie')
async def vitebskaya_obl_drugie(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'vitebskaya-obl-drugie'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Другие города', reply_markup=GO)

@dp.callback_query_handler(text='vsa_gomelstaya')
async def vsa_gomelstaya(message: types.Message):
    await bot.send_message(message.from_user.id, text=f"Выберите подходящий город Гомельской обл. или все для отслеживания:", 
                           reply_markup=GOMELSKAYA_OBL)

@dp.callback_query_handler(text='gomelskaya-obl')
async def gomelskaya_obl(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'gomelskaya-obl'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Всю Гомельскую обл.', reply_markup=GO)

@dp.callback_query_handler(text='gomel')
async def gomel(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'gomel'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Гомель', reply_markup=GO)

@dp.callback_query_handler(text='bragin')
async def bragin(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'bragin'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Брагин', reply_markup=GO)

@dp.callback_query_handler(text='buda-koshelevo')
async def buda_koshelevo(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'buda-koshelevo'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Буда-Кошелево', reply_markup=GO)

@dp.callback_query_handler(text='vasilevichy')
async def vasilevichy(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'vasilevichy'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Василевичи', reply_markup=GO)

@dp.callback_query_handler(text='vetka')
async def vetka(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'vetka'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Ветка', reply_markup=GO)

@dp.callback_query_handler(text='dobrush')
async def dobrush(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'dobrush'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Добруш', reply_markup=GO)

@dp.callback_query_handler(text='elsk')
async def elsk(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'elsk'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Ельск', reply_markup=GO)

@dp.callback_query_handler(text='zhitkovichi')
async def zhitkovichi(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'zhitkovichi'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Житковичи', reply_markup=GO)

@dp.callback_query_handler(text='zhlobin')
async def zhlobin(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'zhlobin'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Жлобин', reply_markup=GO)

@dp.callback_query_handler(text='kalinkovichi')
async def kalinkovichi(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'kalinkovichi'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Калинковичи', reply_markup=GO)

@dp.callback_query_handler(text='korma')
async def korma(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'korma'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Корма', reply_markup=GO)

@dp.callback_query_handler(text='lelchicy')
async def lelchicy(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'lelchicy'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Лельчицы', reply_markup=GO)

@dp.callback_query_handler(text='loev')
async def loev(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'loev'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Лоев', reply_markup=GO)

@dp.callback_query_handler(text='mozyr')
async def mozyr(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'mozyr'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Мозырь', reply_markup=GO)

@dp.callback_query_handler(text='oktyabrskij')
async def oktyabrskij(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'oktyabrskij'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Октябрьский', reply_markup=GO)

@dp.callback_query_handler(text='narovlya')
async def narovlya(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'narovlya'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Наровля', reply_markup=GO)

@dp.callback_query_handler(text='petrikov')
async def petrikov(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'petrikov'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Петриков', reply_markup=GO)

@dp.callback_query_handler(text='rechica')
async def rechica(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'rechica'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Речица', reply_markup=GO)

@dp.callback_query_handler(text='rogachev')
async def rogachev(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'rogachev'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Рогачев', reply_markup=GO)

@dp.callback_query_handler(text='svetlogorsk')
async def svetlogorsk(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'svetlogorsk'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Светлогорск', reply_markup=GO)

@dp.callback_query_handler(text='hojniki')
async def hojniki(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'hojniki'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Хойники', reply_markup=GO)

@dp.callback_query_handler(text='chechersk')
async def chechersk(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'chechersk'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Чечерск', reply_markup=GO)

@dp.callback_query_handler(text='gomelskaya-obl-drugie')
async def gomelskaya_obl_drugie(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'gomelskaya-obl-drugie'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Другие города', reply_markup=GO)

@dp.callback_query_handler(text='vsa_grodnenskaya')
async def vsa_grodnenskaya(message: types.Message):
    await bot.send_message(message.from_user.id, text=f"Выберите подходящий город Гродненской обл. или все для отслеживания:", 
                           reply_markup=GRODNENSKAYA_OBL)

@dp.callback_query_handler(text='grodnenskaya-obl')
async def grodnenskaya_obl(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'grodnenskaya-obl'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Всю Гродненскую обл.', reply_markup=GO)

@dp.callback_query_handler(text='grodno')
async def grodno(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'grodno'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Гродно', reply_markup=GO)

@dp.callback_query_handler(text='berezovka')
async def berezovka(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'berezovka'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Березовка', reply_markup=GO)

@dp.callback_query_handler(text='berestovica')
async def berestovica(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'berestovica'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Берестовица', reply_markup=GO)

@dp.callback_query_handler(text='volkovysk')
async def volkovysk(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'volkovysk'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Волковыск', reply_markup=GO)

@dp.callback_query_handler(text='voronovo')
async def voronovo(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'voronovo'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Вороново', reply_markup=GO)

@dp.callback_query_handler(text='dyatlovo')
async def dyatlovo(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'dyatlovo'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Дятлово', reply_markup=GO)

@dp.callback_query_handler(text='zelva')
async def zelva(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'zelva'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Зельва', reply_markup=GO)

@dp.callback_query_handler(text='ivie')
async def ivie(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'ivie'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Ивье', reply_markup=GO)

@dp.callback_query_handler(text='korelichi')
async def korelichi(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'korelichi'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Кореличи', reply_markup=GO)

@dp.callback_query_handler(text='lida')
async def lida(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'lida'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Лида', reply_markup=GO)

@dp.callback_query_handler(text='mosty')
async def mosty(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'mosty'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Мосты', reply_markup=GO)

@dp.callback_query_handler(text='novogrudok')
async def novogrudok(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'novogrudok'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Новогрудок', reply_markup=GO)

@dp.callback_query_handler(text='ostrovec')
async def ostrovec(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'ostrovec'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Островец', reply_markup=GO)

@dp.callback_query_handler(text='oshmyany')
async def oshmyany(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'oshmyany'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Ошмяны', reply_markup=GO)

@dp.callback_query_handler(text='svisloch')
async def svisloch(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'svisloch'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Свислочь', reply_markup=GO)

@dp.callback_query_handler(text='skidel')
async def skidel(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'skidel'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Скидель', reply_markup=GO)

@dp.callback_query_handler(text='slonim')
async def slonim(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'slonim'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Слоним', reply_markup=GO)

@dp.callback_query_handler(text='smorgon')
async def smorgon(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'smorgon'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Сморгонь', reply_markup=GO)

@dp.callback_query_handler(text='shchuchin')
async def shchuchin(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'shchuchin'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Щучин', reply_markup=GO)

@dp.callback_query_handler(text='grodnenskaya-obl-drugie')
async def grodnenskaya_obl_drugie(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'grodnenskaya-obl-drugie'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Другие города', reply_markup=GO)

@dp.callback_query_handler(text='vsa_minskaya')
async def vsa_minskaya(message: types.Message):
    await bot.send_message(message.from_user.id, text=f"Выберите подходящий город Минской обл. или все для отслеживания:", 
                           reply_markup=MINSKAYA_OBL)

@dp.callback_query_handler(text='minskaya-obl')
async def minskaya_obl(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'minskaya-obl'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Всю Минскую обл.', reply_markup=GO)


@dp.callback_query_handler(text='minskij-rajon')
async def minskij_rajon(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'minskij-rajon'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Минский район', reply_markup=GO)

@dp.callback_query_handler(text='berezino')
async def berezino(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'berezino'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Березино', reply_markup=GO)

@dp.callback_query_handler(text='borisov')
async def borisov(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'borisov'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Борисов', reply_markup=GO)

@dp.callback_query_handler(text='vilejka')
async def vilejka(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'vilejka'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Вилейка', reply_markup=GO)

@dp.callback_query_handler(text='volozhin')
async def volozhin(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'volozhin'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Воложин', reply_markup=GO)

@dp.callback_query_handler(text='dzerzhinsk')
async def dzerzhinsk(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'dzerzhinsk'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Дзержинск', reply_markup=GO)

@dp.callback_query_handler(text='zhodino')
async def zhodino(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'zhodino'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Жодино', reply_markup=GO)

@dp.callback_query_handler(text='zaslavl')
async def zaslavl(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'zaslavl'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Заславль', reply_markup=GO)

@dp.callback_query_handler(text='kleck')
async def kleck(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'kleck'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Клецк', reply_markup=GO)

@dp.callback_query_handler(text='kopyl')
async def kopyl(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'kopyl'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Копыль', reply_markup=GO)

@dp.callback_query_handler(text='krupki')
async def krupki(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'krupki'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Крупки', reply_markup=GO)

@dp.callback_query_handler(text='logojsk')
async def logojsk(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'logojsk'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Логойск', reply_markup=GO)

@dp.callback_query_handler(text='lyuban')
async def lyuban(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'lyuban'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Любань', reply_markup=GO)

@dp.callback_query_handler(text='marina-gorka')
async def marina_gorka(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'marina-gorka'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Марьина Горка', reply_markup=GO)

@dp.callback_query_handler(text='molodechno')
async def molodechno(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'molodechno'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Молодечно', reply_markup=GO)

@dp.callback_query_handler(text='myadel')
async def myadel(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'myadel'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Мядель', reply_markup=GO)

@dp.callback_query_handler(text='nesvizh')
async def nesvizh(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'nesvizh'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Несвиж', reply_markup=GO)

@dp.callback_query_handler(text='rudensk')
async def rudensk(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'rudensk'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Руденск', reply_markup=GO)

@dp.callback_query_handler(text='sluck')
async def sluck(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'sluck'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Слуцк', reply_markup=GO)

@dp.callback_query_handler(text='smolevichi')
async def smolevichi(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'smolevichi'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Смолевичи', reply_markup=GO)

@dp.callback_query_handler(text='soligorsk')
async def soligorsk(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'soligorsk'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Солигорск', reply_markup=GO)

@dp.callback_query_handler(text='starye-dorogi')
async def starye_dorogi(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'starye-dorogi'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Старые Дороги', reply_markup=GO)

@dp.callback_query_handler(text='stolbcy')
async def stolbcy(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'stolbcy'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Столбцы', reply_markup=GO)

@dp.callback_query_handler(text='uzda')
async def uzda(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'uzda'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Узда', reply_markup=GO)

@dp.callback_query_handler(text='fanipol')
async def fanipol(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'fanipol'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Фаниполь', reply_markup=GO)

@dp.callback_query_handler(text='cherven')
async def cherven(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'cherven'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Червень', reply_markup=GO)

@dp.callback_query_handler(text='minskaya-obl-drugie')
async def minskaya_obl_drugie(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'minskaya-obl-drugie'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Другие города', reply_markup=GO)

@dp.callback_query_handler(text='vsa_mogilevskaya')
async def vsa_mogilevskaya(message: types.Message):
    await bot.send_message(message.from_user.id, text=f"Выберите подходящий город Могилевской обл. или все для отслеживания:", 
                           reply_markup=MOGILEVSKAYA_OBL)

@dp.callback_query_handler(text='mogilevskaya-obl')
async def mogilevskaya_obl(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'mogilevskaya-obl'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Всю Могилевскую обл.', reply_markup=GO)

@dp.callback_query_handler(text='mogilev')
async def mogilev(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'mogilev'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Могилев', reply_markup=GO)

@dp.callback_query_handler(text='belynichi')
async def belynichi(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'belynichi'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Белыничи', reply_markup=GO)

@dp.callback_query_handler(text='bobrujsk')
async def bobrujsk(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'bobrujsk'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Бобруйск', reply_markup=GO)

@dp.callback_query_handler(text='byhov')
async def byhov(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'byhov'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Быхов', reply_markup=GO)

@dp.callback_query_handler(text='glusk')
async def glusk(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'glusk'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Глуск', reply_markup=GO)

@dp.callback_query_handler(text='gorki')
async def gorki(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'gorki'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Горки', reply_markup=GO)

@dp.callback_query_handler(text='dribin')
async def dribin(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'dribin'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Дрибин', reply_markup=GO)

@dp.callback_query_handler(text='kirovsk')
async def kirovsk(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'kirovsk'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Кировск', reply_markup=GO)

@dp.callback_query_handler(text='klimovichi')
async def klimovichi(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'klimovichi'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Климовичи', reply_markup=GO)

@dp.callback_query_handler(text='klichev')
async def klichev(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'klichev'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Кличев', reply_markup=GO)

@dp.callback_query_handler(text='krasnopole')
async def krasnopole(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'krasnopole'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Краснополье', reply_markup=GO)

@dp.callback_query_handler(text='krugloe')
async def krugloe(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'krugloe'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Круглое', reply_markup=GO)

@dp.callback_query_handler(text='kostyukovichi')
async def kostyukovichi(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'kostyukovichi'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Костюковичи', reply_markup=GO)

@dp.callback_query_handler(text='krichev')
async def krichev(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'krichev'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Кричев', reply_markup=GO)

@dp.callback_query_handler(text='mstislavl')
async def mstislavl(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'mstislavl'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Мстиславль', reply_markup=GO)

@dp.callback_query_handler(text='osipovichi')
async def osipovichi(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'osipovichi'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Осиповичи', reply_markup=GO)

@dp.callback_query_handler(text='slavgorod')
async def slavgorod(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'slavgorod'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Славгород', reply_markup=GO)

@dp.callback_query_handler(text='chausy')
async def chausy(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'chausy'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Чаусы', reply_markup=GO)

@dp.callback_query_handler(text='cherikov')
async def cherikov(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'cherikov'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Чериков', reply_markup=GO)

@dp.callback_query_handler(text='shklov')
async def shklov(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'shklov'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Шклов', reply_markup=GO)

@dp.callback_query_handler(text='hotimsk')
async def hotimsk(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'hotimsk'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Хотимск', reply_markup=GO)

@dp.callback_query_handler(text='mogilevskaya-obl-drugie')
async def mogilevskaya_obl_drugie(message: types.Message):
    sufix = 'l/r~'
    reg = sufix+'mogilevskaya-obl-drugie'
    all_table = table.all()
    for index in range(len(all_table)):
        if all_table[index]['fields']['UserTGID'] == str(message.from_user.id):
            record_id = all_table[index]['id']
            table.update(record_id=record_id, fields={'Region': str(reg)})
            await bot.send_message(message.from_user.id, text=f'Вы выбрали - Другие города', reply_markup=GO)

