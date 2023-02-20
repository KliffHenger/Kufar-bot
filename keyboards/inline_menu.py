from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


BTN_set_search = InlineKeyboardButton(text='\U0001F4DD Ввести Запрос', callback_data='set_word')
BTN_region_select = InlineKeyboardButton(text='\U0001F5FA Изменить Регион', callback_data='region_select')
BTN_go_search = InlineKeyboardButton(text='\U0001F50E Начать Отслеживание', callback_data='start_search')
BTN_stop_search = InlineKeyboardButton(text='\U0001F6D1 Остановить Отслеживание', callback_data='stop_search')
BTN_menu = InlineKeyboardButton(text='\U000026A1 Вывести Меню \U000026A1', callback_data='menu')
# BTN_ = InlineKeyboardButton(text='', callback_data='')


START = InlineKeyboardMarkup().add(BTN_set_search)
ALL_MENU = InlineKeyboardMarkup().add(BTN_set_search).add(BTN_region_select).add(BTN_go_search).add(BTN_stop_search)
MENU = InlineKeyboardMarkup().add(BTN_menu)
GO = InlineKeyboardMarkup().add(BTN_go_search)
STOP = InlineKeyboardMarkup().add(BTN_stop_search)
REGION = InlineKeyboardMarkup().add(BTN_region_select, BTN_go_search)