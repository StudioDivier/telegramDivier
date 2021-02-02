from telebot import types


def hello_keyboard():
    hello_keyb = types.InlineKeyboardMarkup()
    h_send_form = types.InlineKeyboardButton(text='\U0001F4DD Оставить заявку', callback_data='h_send_form')
    h_calc = types.InlineKeyboardButton(text='\U0001F4E5 Собрать заказ', callback_data='to_lvl2')
    hello_keyb.add(h_send_form)
    hello_keyb.add(h_calc)
    return hello_keyb


def send_phone_keyboard():
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)  # Подключаем клавиатуру
    button_phone = types.KeyboardButton(text="\U0001F4DE Отправить телефон", request_contact=True)
    keyboard.add(button_phone)  # Добавляем эту кнопку
    return keyboard


def to_start():
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)  # Подключаем клавиатуру
    button_phone = types.KeyboardButton(text="Отправиться нас старт.", )
    keyboard.add(button_phone)  # Добавляем эту кнопку
    return keyboard


# level 2
def choice_1():
    keyboard = types.InlineKeyboardMarkup()
    key = types.InlineKeyboardButton(text='\U0001F511 Под ключ', callback_data='on_key')
    dis = types.InlineKeyboardButton(text='\U0001F3A8 Дизайн/Редизайн', callback_data='dis')
    supp = types.InlineKeyboardButton(text='\U0001F527 Доработка/Поддержка', callback_data='supp')
    opt = types.InlineKeyboardButton(text='\U0001F947 Продвижение/ Оптимизация', callback_data='opt')
    ad = types.InlineKeyboardButton(text='\U0001F3AF Реклама', callback_data='adv')
    port = types.InlineKeyboardButton('Смотреть наше портфолио\U0001F5C2', url='https://www.divier.ru/portfolio/sozdanie_saytov/')
    keyboard.add(key)
    keyboard.add(dis)
    keyboard.add(supp)
    keyboard.add(opt)
    keyboard.add(ad)
    keyboard.add(port)
    return keyboard


# level 3
def choice_1_1():
    keyboard = types.InlineKeyboardMarkup()
    site = types.InlineKeyboardButton(text='\U0001F5A5 Сайт', callback_data='site')
    mob_app = types.InlineKeyboardButton(text='\U0001F4F2 Мобильное приложение', callback_data='mob_app')
    all = types.InlineKeyboardButton(text='\U0001F5A5 И то \U0001F4F2 и то', callback_data='all')
    back = types.InlineKeyboardButton(text='\U00002B05 Вернуться назад', callback_data='to_lvl2')
    keyboard.add(site)
    keyboard.add(mob_app)
    keyboard.add(all)
    keyboard.add(back)
    return keyboard


def choice_1_2():
    keyboard = types.InlineKeyboardMarkup()
    new_design = types.InlineKeyboardButton(text='\U0001F3A8 Новый дизайн', callback_data='new_design')
    old_design = types.InlineKeyboardButton(text='\U0001F527 Доработка дизайна текущего', callback_data='old_design')
    cons = types.InlineKeyboardButton(text='\U0001F4DE Консультация', callback_data='cons12')
    back = types.InlineKeyboardButton(text='\U00002B05 Вернуться назад', callback_data='to_lvl2')
    keyboard.add(new_design)
    keyboard.add(old_design)
    keyboard.add(cons)
    keyboard.add(back)
    return keyboard


def choice_1_3():
    keyboard = types.InlineKeyboardMarkup()
    refactoring = types.InlineKeyboardButton(text='\U0001F527 Разовые доработки', callback_data='refactoring')
    tech_support = types.InlineKeyboardButton(text='\U0001F6E0 Тех.поддержка', callback_data='tech_support')
    integration = types.InlineKeyboardButton(text='\U0001F4C8 Интеграция 1С', callback_data='integration')
    payment = types.InlineKeyboardButton(text='\U0001F4B8 Платежные системы', callback_data='payment')
    cons = types.InlineKeyboardButton(text='\U0001F4DE Консультация', callback_data='cons13')
    back = types.InlineKeyboardButton(text='\U00002B05 Вернуться назад', callback_data='to_lvl2')
    keyboard.add(refactoring)
    keyboard.add(tech_support)
    keyboard.add(integration)
    keyboard.add(payment)
    keyboard.add(cons)
    keyboard.add(back)
    return keyboard


def choice_1_4():
    keyboard = types.InlineKeyboardMarkup()
    search = types.InlineKeyboardButton(text='\U0001F51D Продвижение в поиске', callback_data='search')
    seo = types.InlineKeyboardButton(text='\U00002699 Разовая SEO', callback_data='seo')
    cons = types.InlineKeyboardButton(text='\U0001F4DE Консультация', callback_data='cons14')
    back = types.InlineKeyboardButton(text='\U00002B05 Вернуться назад', callback_data='to_lvl2')
    keyboard.add(search)
    keyboard.add(seo)
    keyboard.add(cons)
    keyboard.add(back)
    return keyboard


def choice_1_5():
    keyboard = types.InlineKeyboardMarkup()
    yandex = types.InlineKeyboardButton(text='\U0001F4D2 Яндекс.Директ', callback_data='yandex')
    google = types.InlineKeyboardButton(text='\U0001F4D8 Google Ad', callback_data='google')
    smm = types.InlineKeyboardButton(text='\U0001F4CA SMM', callback_data='smm')
    all = types.InlineKeyboardButton(text='\U0001F525 Нужно все', callback_data='all15')
    cons = types.InlineKeyboardButton(text='\U0001F4DE Консультация', callback_data='cons15')
    back = types.InlineKeyboardButton(text='\U00002B05 Вернуться назад', callback_data='to_lvl2')
    keyboard.add(yandex)
    keyboard.add(google)
    keyboard.add(smm)
    keyboard.add(all)
    keyboard.add(cons)
    keyboard.add(back)
    return keyboard


# level 4
def choice_1_1_site():
    keyboard = types.InlineKeyboardMarkup()
    company = types.InlineKeyboardButton(text='\U0001F4BC Сайт компании', callback_data='company')
    eshop = types.InlineKeyboardButton(text='\U0001F3EC Интернет магазин', callback_data='eshop')
    info = types.InlineKeyboardButton(text='\U0001F50D Информационный сайт', callback_data='info')
    lending = types.InlineKeyboardButton(text='\U0001F6EC Лендинг', callback_data='lending')
    back = types.InlineKeyboardButton(text='\U00002B05 Вернуться назад', callback_data='on_key')
    keyboard.add(company)
    keyboard.add(eshop)
    keyboard.add(info)
    keyboard.add(lending)
    keyboard.add(back)
    return keyboard


