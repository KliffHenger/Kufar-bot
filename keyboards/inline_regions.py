from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup





'''кнопки предвыбора региона'''
BTN_all_minsk = InlineKeyboardButton(text='Минск', callback_data='ves_minsk')
BTN_all_brestskaya = InlineKeyboardButton(text='Брестская обл.', callback_data='vsa_brestskaya')
BTN_all_vitebskaya = InlineKeyboardButton(text='Витебская обл.', callback_data='vsa_vitebslaya')
BTN_all_gomelskaya = InlineKeyboardButton(text='Гомельская обл.', callback_data='vsa_gomelstaya')
BTN_all_grodnenskaya = InlineKeyboardButton(text='Гродненская обл.', callback_data='vsa_grodnenskaya')
BTN_all_mogilevskaya = InlineKeyboardButton(text='Могилевскя обл.', callback_data='vsa_mogilevskaya')
BTN_all_minskaya = InlineKeyboardButton(text='Минская обл.', callback_data='vsa_minskaya')


'''непосредственный выбор всей РБ, Минска и областей по одной для поиска'''
BTN_set_belarus = InlineKeyboardButton(text='Выбрать всю Беларусь', callback_data='vsya_belarus')
BTN_set_minsk = InlineKeyboardButton(text='Весь Минск', callback_data='minsk')
BTN_set_brestskaya_obl = InlineKeyboardButton(text='Вся Брестская обл.', callback_data='brestskaya-obl')
BTN_set_vitebskaya_obl = InlineKeyboardButton(text='Вся Витебская обл.', callback_data='vitebskaya-obl')
BTN_set_gomelskaya_obl = InlineKeyboardButton(text='Вся Гомельская обл.', callback_data='gomelskaya-obl')
BTN_set_grodnenskaya_obl = InlineKeyboardButton(text='Вся Гродненская обл.', callback_data='grodnenskaya-obl')
BTN_set_minskaya_obl = InlineKeyboardButton(text='Вся Минская обл.', callback_data='minskaya-obl')
BTN_set_mogilevskaya_obl = InlineKeyboardButton(text='Вся Могилевская обл.', callback_data='mogilevskaya-obl')



"""непосредственный выбор районов Минска"""
BTN_set_minsk_centralnyj = InlineKeyboardButton(text='Минск, Центральный р-н', callback_data='minsk-centralnyj')
BTN_set_minsk_sovetskij = InlineKeyboardButton(text='Минск, Советский р-н', callback_data='minsk-sovetskij')
BTN_set_mins_pervomajskij = InlineKeyboardButton(text='Минск, Первомайский р-н', callback_data='mins-pervomajskij')
BTN_set_minsk_partizanskij = InlineKeyboardButton(text='Минск, Партизанский р-н', callback_data='minsk-partizanskij')
BTN_set_minsk_zavodskoj = InlineKeyboardButton(text='Минск, Заводской р-н', callback_data='minsk-zavodskoj')
BTN_set_minsk_leninskij = InlineKeyboardButton(text='Минск, Ленинский р-н', callback_data='minsk-leninskij')
BTN_set_minsk_oktyabrskij = InlineKeyboardButton(text='Минск, Октябрьский р-н', callback_data='minsk-oktyabrskij')
BTN_set_minsk_moskovskij = InlineKeyboardButton(text='Минск, Московский р-н', callback_data='minsk-moskovskij')
BTN_set_minsk_frunzenskij = InlineKeyboardButton(text='Минск, Фрунзенский р-н', callback_data='minsk-frunzenskij')
"""непосредственный выбор городов Брестской области"""
BTN_set_brest = InlineKeyboardButton(text='Брест', callback_data='brest')
BTN_set_baranovichi = InlineKeyboardButton(text='Барановичи', callback_data='baranovichi')
BTN_set_bereza = InlineKeyboardButton(text='Береза', callback_data='bereza')
BTN_set_beloozersk = InlineKeyboardButton(text='Белоозерск', callback_data='beloozersk')
BTN_set_vysokae = InlineKeyboardButton(text='Высокое', callback_data='vysokae')
BTN_set_gancevichi = InlineKeyboardButton(text='Ганцевичи', callback_data='gancevichi')
BTN_set_davyd_haradok = InlineKeyboardButton(text='Давид-Городок', callback_data='davyd-haradok')
BTN_set_drogichin = InlineKeyboardButton(text='Дрогичин', callback_data='drogichin')
BTN_set_zhabinka = InlineKeyboardButton(text='Жабинка', callback_data='zhabinka')
BTN_set_ivanovo = InlineKeyboardButton(text='Иваново', callback_data='ivanovo')
BTN_set_ivacevichi = InlineKeyboardButton(text='Ивацевичи', callback_data='ivacevichi')
BTN_set_kamenec = InlineKeyboardButton(text='Каменец', callback_data='kamenec')
BTN_set_kobrin = InlineKeyboardButton(text='Кобрин', callback_data='kobrin')
BTN_set_luninec = InlineKeyboardButton(text='Лунинец', callback_data='luninec')
BTN_set_lyahovichi = InlineKeyboardButton(text='Ляховичи', callback_data='lyahovichi')
BTN_set_malorita = InlineKeyboardButton(text='Малорита', callback_data='malorita')
BTN_set_mikashevichy = InlineKeyboardButton(text='Микашевичи', callback_data='mikashevichy')
BTN_set_pinsk = InlineKeyboardButton(text='Пинск', callback_data='pinsk')
BTN_set_pruzhany = InlineKeyboardButton(text='Пружаны', callback_data='pruzhany')
BTN_set_stolin = InlineKeyboardButton(text='Столин', callback_data='stolin')
BTN_set_brestskaya_obl_drugie = InlineKeyboardButton(text='Другие города', callback_data='brestskaya-obl-drugie')
"""непосредственный выбор городов Витебской области"""
BTN_set_vitebsk = InlineKeyboardButton(text='Витебск', callback_data='vitebsk')
BTN_set_beshenkovichi = InlineKeyboardButton(text='Бешенковичи', callback_data='beshenkovichi')
BTN_set_baran = InlineKeyboardButton(text='Барань', callback_data='baran')
BTN_set_braslav = InlineKeyboardButton(text='Браслав', callback_data='braslav')
BTN_set_verhnedvinsk = InlineKeyboardButton(text='Верхнедвинск', callback_data='verhnedvinsk')
BTN_set_glubokoe = InlineKeyboardButton(text='Глубокое', callback_data='glubokoe')
BTN_set_gorodok = InlineKeyboardButton(text='Городок', callback_data='gorodok')
BTN_set_dubrovno = InlineKeyboardButton(text='Дубровно', callback_data='dubrovno')
BTN_set_lepel = InlineKeyboardButton(text='Лепель', callback_data='lepel')
BTN_set_liozno = InlineKeyboardButton(text='Лиозно', callback_data='liozno')
BTN_set_miory = InlineKeyboardButton(text='Миоры', callback_data='miory')
BTN_set_novolukoml = InlineKeyboardButton(text='Новолукомль', callback_data='novolukoml')
BTN_set_novopolock = InlineKeyboardButton(text='Новополоцк', callback_data='novopolock')
BTN_set_orsha = InlineKeyboardButton(text='Орша', callback_data='orsha')
BTN_set_polock = InlineKeyboardButton(text='Полоцк', callback_data='polock')
BTN_set_postavy = InlineKeyboardButton(text='Поставы', callback_data='postavy')
BTN_set_rossony = InlineKeyboardButton(text='Россоны', callback_data='rossony')
BTN_set_senno = InlineKeyboardButton(text='Сенно', callback_data='senno')
BTN_set_tolochin = InlineKeyboardButton(text='Толочин', callback_data='tolochin')
BTN_set_ushachi = InlineKeyboardButton(text='Ушачи', callback_data='ushachi')
BTN_set_chashniki = InlineKeyboardButton(text='Чашники', callback_data='chashniki')
BTN_set_sharkovshchina = InlineKeyboardButton(text='Шарковщина', callback_data='sharkovshchina')
BTN_set_shumilino = InlineKeyboardButton(text='Шумилино', callback_data='shumilino')
BTN_set_vitebskaya_obl_drugie = InlineKeyboardButton(text='Другие города', callback_data='vitebskaya-obl-drugie')
"""непосредственный выбор городов Гомельской области"""
BTN_set_gomel = InlineKeyboardButton(text='Гомель', callback_data='gomel')
BTN_set_bragin = InlineKeyboardButton(text='Брагин', callback_data='bragin')
BTN_set_buda_koshelevo = InlineKeyboardButton(text='Буда-Кошелево', callback_data='buda-koshelevo')
BTN_set_vasilevichy = InlineKeyboardButton(text='Василевичи', callback_data='vasilevichy')
BTN_set_vetka = InlineKeyboardButton(text='Ветка', callback_data='vetka')
BTN_set_dobrush = InlineKeyboardButton(text='Добруш', callback_data='dobrush')
BTN_set_elsk = InlineKeyboardButton(text='Ельск', callback_data='elsk')
BTN_set_zhitkovichi = InlineKeyboardButton(text='Житковичи', callback_data='zhitkovichi')
BTN_set_zhlobin = InlineKeyboardButton(text='Жлобин', callback_data='zhlobin')
BTN_set_kalinkovichi = InlineKeyboardButton(text='Калинковичи', callback_data='kalinkovichi')
BTN_set_korma = InlineKeyboardButton(text='Корма', callback_data='korma')
BTN_set_lelchicy = InlineKeyboardButton(text='Лельчицы', callback_data='lelchicy')
BTN_set_loev = InlineKeyboardButton(text='Лоев', callback_data='loev')
BTN_set_mozyr = InlineKeyboardButton(text='Мозырь', callback_data='mozyr')
BTN_set_oktyabrskij = InlineKeyboardButton(text='Октябрьский', callback_data='oktyabrskij')
BTN_set_narovlya = InlineKeyboardButton(text='Наровля', callback_data='narovlya')
BTN_set_petrikov = InlineKeyboardButton(text='Петриков', callback_data='petrikov')
BTN_set_rechica = InlineKeyboardButton(text='Речица', callback_data='rechica')
BTN_set_rogachev = InlineKeyboardButton(text='Рогачев', callback_data='rogachev')
BTN_set_svetlogorsk = InlineKeyboardButton(text='Светлогорск', callback_data='svetlogorsk')
BTN_set_hojniki = InlineKeyboardButton(text='Хойники', callback_data='hojniki')
BTN_set_chechersk = InlineKeyboardButton(text='Чечерск', callback_data='chechersk')
BTN_set_gomelskaya_obl_drugie = InlineKeyboardButton(text='Другие города', callback_data='gomelskaya-obl-drugie')
"""непосредственный выбор городов Гродненской области"""
BTN_set_grodno = InlineKeyboardButton(text='Гродно', callback_data='grodno')
BTN_set_berezovka = InlineKeyboardButton(text='Березовка', callback_data='berezovka')
BTN_set_berestovica = InlineKeyboardButton(text='Берестовица', callback_data='berestovica')
BTN_set_volkovysk = InlineKeyboardButton(text='Волковыск', callback_data='volkovysk')
BTN_set_voronovo = InlineKeyboardButton(text='Вороново', callback_data='voronovo')
BTN_set_dyatlovo = InlineKeyboardButton(text='Дятлово', callback_data='dyatlovo')
BTN_set_zelva = InlineKeyboardButton(text='Зельва', callback_data='zelva')
BTN_set_ivie = InlineKeyboardButton(text='Ивье', callback_data='ivie')
BTN_set_korelichi = InlineKeyboardButton(text='Кореличи', callback_data='korelichi')
BTN_set_lida = InlineKeyboardButton(text='Лида', callback_data='lida')
BTN_set_mosty = InlineKeyboardButton(text='Мосты', callback_data='mosty')
BTN_set_novogrudok = InlineKeyboardButton(text='Новогрудок', callback_data='novogrudok')
BTN_set_ostrovec = InlineKeyboardButton(text='Островец', callback_data='ostrovec')
BTN_set_oshmyany = InlineKeyboardButton(text='Ошмяны', callback_data='oshmyany')
BTN_set_svisloch = InlineKeyboardButton(text='Свислочь', callback_data='svisloch')
BTN_set_skidel = InlineKeyboardButton(text='Скидель', callback_data='skidel')
BTN_set_slonim = InlineKeyboardButton(text='Слоним', callback_data='slonim')
BTN_set_smorgon = InlineKeyboardButton(text='Сморгонь', callback_data='smorgon')
BTN_set_shchuchin = InlineKeyboardButton(text='Щучин', callback_data='shchuchin')
BTN_set_grodnenskaya_obl_drugie = InlineKeyboardButton(text='Другие города', callback_data='grodnenskaya-obl-drugie')
"""непосредственный выбор городов Могилевской области"""
BTN_set_mogilev = InlineKeyboardButton(text='Могилев', callback_data='mogilev')
BTN_set_belynichi = InlineKeyboardButton(text='Белыничи', callback_data='belynichi')
BTN_set_bobrujsk = InlineKeyboardButton(text='Бобруйск', callback_data='bobrujsk')
BTN_set_byhov = InlineKeyboardButton(text='Быхов', callback_data='byhov')
BTN_set_glusk = InlineKeyboardButton(text='Глуск', callback_data='glusk')
BTN_set_gorki = InlineKeyboardButton(text='Горки', callback_data='gorki')
BTN_set_dribin = InlineKeyboardButton(text='Дрибин', callback_data='dribin')
BTN_set_kirovsk = InlineKeyboardButton(text='Кировск', callback_data='kirovsk')
BTN_set_klimovichi = InlineKeyboardButton(text='Климовичи', callback_data='klimovichi')
BTN_set_klichev = InlineKeyboardButton(text='Кличев', callback_data='klichev')
BTN_set_krasnopole = InlineKeyboardButton(text='Краснополье', callback_data='krasnopole')
BTN_set_krugloe = InlineKeyboardButton(text='Круглое', callback_data='krugloe')
BTN_set_kostyukovichi = InlineKeyboardButton(text='Костюковичи', callback_data='kostyukovichi')
BTN_set_krichev = InlineKeyboardButton(text='Кричев', callback_data='krichev')
BTN_set_mstislavl = InlineKeyboardButton(text='Мстиславль', callback_data='mstislavl')
BTN_set_osipovichi = InlineKeyboardButton(text='Осиповичи', callback_data='osipovichi')
BTN_set_slavgorod = InlineKeyboardButton(text='Славгород', callback_data='slavgorod')
BTN_set_chausy = InlineKeyboardButton(text='Чаусы', callback_data='chausy')
BTN_set_cherikov = InlineKeyboardButton(text='Чериков', callback_data='cherikov')
BTN_set_shklov = InlineKeyboardButton(text='Шклов', callback_data='shklov')
BTN_set_hotimsk = InlineKeyboardButton(text='Хотимск', callback_data='hotimsk')
BTN_set_mogilevskaya_obl_drugie = InlineKeyboardButton(text='Другие города', callback_data='mogilevskaya-obl-drugie')
"""непосредственный выбор городов Минской области"""
BTN_set_minskij_rajon = InlineKeyboardButton(text='Минский район', callback_data='minskij-rajon')
BTN_set_berezino = InlineKeyboardButton(text='Березино', callback_data='berezino')
BTN_set_borisov = InlineKeyboardButton(text='Борисов', callback_data='borisov')
BTN_set_vilejka = InlineKeyboardButton(text='Вилейка', callback_data='vilejka')
BTN_set_volozhin = InlineKeyboardButton(text='Воложин', callback_data='volozhin')
BTN_set_dzerzhinsk = InlineKeyboardButton(text='Дзержинск', callback_data='dzerzhinsk')
BTN_set_zhodino = InlineKeyboardButton(text='Жодино', callback_data='zhodino')
BTN_set_zaslavl = InlineKeyboardButton(text='Заславль', callback_data='zaslavl')
BTN_set_kleck = InlineKeyboardButton(text='Клецк', callback_data='kleck')
BTN_set_kopyl = InlineKeyboardButton(text='Копыль', callback_data='kopyl')
BTN_set_krupki = InlineKeyboardButton(text='Крупки', callback_data='krupki')
BTN_set_logojsk = InlineKeyboardButton(text='Логойск', callback_data='logojsk')
BTN_set_lyuban = InlineKeyboardButton(text='Любань', callback_data='lyuban')
BTN_set_marina_gorka = InlineKeyboardButton(text='Марьина Горка', callback_data='marina-gorka')
BTN_set_molodechno = InlineKeyboardButton(text='Молодечно', callback_data='molodechno')
BTN_set_myadel = InlineKeyboardButton(text='Мядель', callback_data='myadel')
BTN_set_nesvizh = InlineKeyboardButton(text='Несвиж', callback_data='nesvizh')
BTN_set_rudensk = InlineKeyboardButton(text='Руденск', callback_data='rudensk')
BTN_set_sluck = InlineKeyboardButton(text='Слуцк', callback_data='sluck')
BTN_set_smolevichi = InlineKeyboardButton(text='Смолевичи', callback_data='smolevichi')
BTN_set_soligorsk = InlineKeyboardButton(text='Солигорск', callback_data='soligorsk')
BTN_set_starye_dorogi = InlineKeyboardButton(text='Старые Дороги', callback_data='starye-dorogi')
BTN_set_stolbcy = InlineKeyboardButton(text='Столбцы', callback_data='stolbcy')
BTN_set_uzda = InlineKeyboardButton(text='Узда', callback_data='uzda')
BTN_set_fanipol = InlineKeyboardButton(text='Фаниполь', callback_data='fanipol')
BTN_set_cherven = InlineKeyboardButton(text='Червень', callback_data='cherven')
BTN_set_minskaya_obl_drugie = InlineKeyboardButton(text='Другие города', callback_data='minskaya-obl-drugie')



REGIONS = InlineKeyboardMarkup().add(BTN_set_belarus, BTN_all_minsk).add(BTN_all_brestskaya, BTN_all_vitebskaya)\
    .add(BTN_all_gomelskaya, BTN_all_grodnenskaya).add(BTN_all_mogilevskaya, BTN_all_minskaya)

MINSK = InlineKeyboardMarkup().add(BTN_set_minsk).add(BTN_set_minsk_centralnyj, BTN_set_minsk_sovetskij)\
    .add(BTN_set_mins_pervomajskij, BTN_set_minsk_partizanskij).add(BTN_set_minsk_zavodskoj, BTN_set_minsk_leninskij)\
    .add(BTN_set_minsk_oktyabrskij, BTN_set_minsk_moskovskij).add(BTN_set_minsk_frunzenskij)

BRESTSKAYA_OBL = InlineKeyboardMarkup().add(BTN_set_brestskaya_obl, BTN_set_brest).add(BTN_set_baranovichi, BTN_set_bereza)\
    .add(BTN_set_beloozersk, BTN_set_vysokae).add(BTN_set_gancevichi, BTN_set_davyd_haradok).add(BTN_set_drogichin, BTN_set_zhabinka)\
    .add(BTN_set_ivanovo, BTN_set_ivacevichi).add(BTN_set_kamenec, BTN_set_kobrin).add(BTN_set_luninec, BTN_set_lyahovichi)\
    .add(BTN_set_malorita, BTN_set_mikashevichy).add(BTN_set_pinsk, BTN_set_pruzhany).add(BTN_set_stolin, BTN_set_brestskaya_obl_drugie)

VITEBSKAYA_OBL = InlineKeyboardMarkup().add(BTN_set_vitebskaya_obl, BTN_set_vitebsk).add(BTN_set_beshenkovichi, BTN_set_baran)\
    .add(BTN_set_braslav, BTN_set_verhnedvinsk).add(BTN_set_glubokoe, BTN_set_gorodok).add(BTN_set_dubrovno, BTN_set_lepel)\
    .add(BTN_set_liozno, BTN_set_miory).add(BTN_set_novolukoml, BTN_set_novopolock).add(BTN_set_orsha, BTN_set_polock)\
    .add(BTN_set_postavy, BTN_set_rossony).add(BTN_set_senno, BTN_set_tolochin).add(BTN_set_ushachi, BTN_set_chashniki)\
    .add(BTN_set_sharkovshchina, BTN_set_shumilino).add(BTN_set_vitebskaya_obl_drugie)

GOMELSKAYA_OBL = InlineKeyboardMarkup().add(BTN_set_gomelskaya_obl, BTN_set_gomel).add(BTN_set_bragin, BTN_set_buda_koshelevo)\
    .add(BTN_set_vasilevichy, BTN_set_vetka).add(BTN_set_dobrush, BTN_set_elsk).add(BTN_set_zhitkovichi, BTN_set_zhlobin)\
    .add(BTN_set_kalinkovichi, BTN_set_korma).add(BTN_set_lelchicy, BTN_set_loev).add(BTN_set_mozyr, BTN_set_oktyabrskij)\
    .add(BTN_set_narovlya, BTN_set_petrikov).add(BTN_set_rechica, BTN_set_rogachev).add(BTN_set_svetlogorsk, BTN_set_hojniki)\
    .add(BTN_set_chechersk, BTN_set_gomelskaya_obl_drugie)

GRODNENSKAYA_OBL = InlineKeyboardMarkup().add(BTN_set_grodnenskaya_obl, BTN_set_grodno).add(BTN_set_berezovka, BTN_set_berestovica)\
    .add(BTN_set_volkovysk, BTN_set_voronovo).add(BTN_set_dyatlovo, BTN_set_zelva).add(BTN_set_ivie, BTN_set_korelichi)\
    .add(BTN_set_lida, BTN_set_mosty).add(BTN_set_novogrudok, BTN_set_ostrovec).add(BTN_set_oshmyany, BTN_set_svisloch)\
    .add(BTN_set_skidel, BTN_set_slonim).add(BTN_set_smorgon, BTN_set_shchuchin).add(BTN_set_grodnenskaya_obl_drugie)

MINSKAYA_OBL = InlineKeyboardMarkup().add(BTN_set_minskaya_obl, BTN_set_minsk).add(BTN_set_minskij_rajon, BTN_set_berezino)\
    .add(BTN_set_borisov, BTN_set_vilejka).add(BTN_set_volozhin, BTN_set_dzerzhinsk).add(BTN_set_zhodino, BTN_set_zaslavl)\
    .add(BTN_set_kleck, BTN_set_kopyl).add(BTN_set_krupki, BTN_set_logojsk).add(BTN_set_lyuban, BTN_set_marina_gorka)\
    .add(BTN_set_molodechno, BTN_set_myadel).add(BTN_set_nesvizh, BTN_set_rudensk).add(BTN_set_sluck, BTN_set_smolevichi)\
    .add(BTN_set_soligorsk, BTN_set_starye_dorogi).add(BTN_set_stolbcy, BTN_set_uzda).add(BTN_set_fanipol, BTN_set_cherven)\
    .add(BTN_set_minskaya_obl_drugie)

MOGILEVSKAYA_OBL = InlineKeyboardMarkup().add(BTN_set_mogilevskaya_obl, BTN_set_mogilev).add(BTN_set_belynichi,BTN_set_bobrujsk)\
    .add(BTN_set_byhov, BTN_set_glusk).add(BTN_set_gorki, BTN_set_dribin).add(BTN_set_kirovsk, BTN_set_klimovichi)\
    .add(BTN_set_klichev, BTN_set_krasnopole).add(BTN_set_krugloe, BTN_set_kostyukovichi).add(BTN_set_krichev, BTN_set_mstislavl)\
    .add(BTN_set_osipovichi, BTN_set_slavgorod).add(BTN_set_chausy, BTN_set_cherikov).add(BTN_set_shklov, BTN_set_hotimsk)\
    .add(BTN_set_mogilevskaya_obl_drugie)

