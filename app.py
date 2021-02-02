#!/usr/bin/env python
# -*- coding: utf-8 -*-
import settings
from threading import Thread
from keyboards import keyb
from services import mailing

from loguru import logger
import telebot

API_TOKEN = settings.TOKEN

# create bot
bot = telebot.TeleBot(settings.TOKEN)

logger.add("log/log.json", level="DEBUG", format="{time} {level} {message}", serialize=True,
           rotation="1 MB", compression="zip")


# Handle '/start' and '/help'
@logger.catch()
@bot.message_handler(commands=['help', 'start'])
def message_start(message):
    kb = telebot.types.InlineKeyboardMarkup()
    # btn = telebot.types.InlineKeyboardButton(text='Нажать чтобы увидеть что я могу', callback_data='start')
    # kb.add(btn)
    kb.add(telebot.types.InlineKeyboardButton('Наш сайт\U0001F4BB', url='https://www.divier.ru/'))
    text_msg = u'\U0001F64B' + ' Привет! Я телеграм бот веб студии *Divier* !\n\n' \
                               'Мы с 2006 г. специализируемся на создании сайтов, работаем с клиентами по всей России\U0001F44B\n' \
                               '\U0001F4D1 Покажу Вам какие услуги мы предоставляем и \n' \
                               '\U0000231A помогу быстро составить заявку для обратной связи!\n\n' \
                               'Ниже нажмите одну из клавиш:\n' \
                               '\U0001F449 если вы хотите посмотреть список услуг, то нажмите на кнопку "Собрать заказ"\n' \
                               '\U0001F449 если вы хотите только оставить заявку, то нажмите неа кнопку "Оставить заявку"\n'
    bot.send_message(
        message.chat.id,
        text_msg,
        reply_markup=kb,
        parse_mode='Markdown'
    )
    text_msg1 = 'Что бы вы хотели?'
    bot.send_message(
        message.chat.id,
        text_msg1,
        reply_markup=keyb.hello_keyboard()
    )

    @bot.callback_query_handler(func=lambda call: True)
    def handle_query(call):
        ######################################
        # level 1
        if call.data == 'h_send_form':
            msg = 'Оставьте свой номер для связи.'
            bot.send_message(message.chat.id, msg, reply_markup=keyb.send_phone_keyboard())

            @bot.message_handler(content_types=['contact'])
            def contact(message):
                id = 'Форма из стартового меню'
                data = {
                    'phone': message.contact.phone_number,
                    'user_name': message.contact.first_name,
                    'call': id
                }

                if mailing.send_mail(data=data):
                    bot.answer_callback_query(call.id, show_alert=True, text="Ваша заявка успешно отправлена!")
                    bot.send_message(message.chat.id, 'Ваша заявка успешно отправлена!',
                                     reply_markup=keyb.hello_keyboard())
                else:
                    bot.send_photo(message.chat.id, get("hhttps://vetliva.ru/upload/iblock/c57/c57d489ec51709bbd60722877685e058.jpg").content)
                    bot.send_message(message.chat.id, 'Упс, что-то пошло не так!\n Но скоро мы все исправим!\n\n'
                                                      'Вы можете позвонить нам или написать на почту:'
                                                      '\U0001F4E7 *_viksne@divier.ru_*'
                                                      '\U0000260E *_8(499)1106264_*'
                                                      '\U0001F4DE *_8(905)5463988_*', reply_markup=keyb.hello_keyboard(), parse_mode='Markdown')

        elif call.data == 'to_lvl2':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text='Мы предлагаем уважаемым заказчикам подготовку и размещение в Сети маркетингового '
                                       'инструмента, приносящего постоянный доход \U0001F4B0\n'
                                       'Комплекс мероприятий это подготовка интерфейса, верстка и интеграция с системой управления, '
                                       'веб программирование любой сложности, seo мероприятия, сопровождение в эксплуатации\U0001F504', reply_markup=keyb.choice_1())

        ######################################
        # level 2
        # под ключ
        elif call.data == 'on_key':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text='Оказываем услуги по созданию сайтов под ключ\U0001F511\n '
                                       'В нашем исполнении это будет проект, который при запуске в эксплуатацию:\n'
                                       '\U0001F53A готов к SEO продвижению и проведению рекламных кампаний\n'
                                       '\U0001F53A не требует дополнительных доработок, поскольку является самодостаточным инструментом маркетинга\n'
                                       '\U0001F53A предназначенным для ведения бизнеса в Сети и привлечения клиентов!\n', reply_markup=keyb.choice_1_1())

        # дизайн
        elif call.data == 'dis':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text='\U0001F4F2 Мобильные приложения, адаптивный интерфейс\n'
                                       'Делаем проекты, которые решают поставленные коммерческие задачи и вызывают положительные эмоции. ',
                                  reply_markup=keyb.choice_1_2())

        # поддержка
        elif call.data == 'supp':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text='\U0001FA7A Продлеваем жизнь ресурсов, сопровождая как существующие технические параметры,\n'
                                       '\U0001F527 так и улучшая их, тем самым позволяя интернет представительству оставаться '
                                       'актуальным в долгосрочном периоде\U000026A1', reply_markup=keyb.choice_1_3())

        # оптимизация
        elif call.data == 'opt':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text='\U0001F4C8 Обеспечим стабильный приток целевых посетителей из поисковых систем Яндекс и Гугл '
                                       'и мотивируем их к контакту.\n'
                                       'Органическая выдача поисковиков, несмотря на регулярно сменяющиеся алгоритмы ранжирования,'
                                       'всегда будет основой целевого трафика и посещаемости.\n'
                                       '\U0001F4CD Приведем веб систему в наилучшее состояние всех её показателей, '
                                       'благодаря чему поисковые системы будут благосклонны к ресурсу при ранжировании,'
                                       'тем самым, достигаем наивысшего результата с учетом минимальных ресурсных затрат', reply_markup=keyb.choice_1_4())

        # реклама
        elif call.data == 'adv':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text='\U0001F9F2 Комплексный интернет маркетинг для стабильного положения веб ресурсов наших '
                                       'заказчиков.\n \U0001F51DЭффективные контекстные и медийные кампании, '
                                       'популяризация в социальных сетях (SMO)', reply_markup=keyb.choice_1_5())

        ######################################
        ###################
        #
        # level 3 point 1 - Под ключ
        # level 3 - from on_key - site
        elif call.data == 'site':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text='\U0001F51DСоздание и продвижение сайтов для разных видов и направлений деятельности.\n'
                                       '\U0001F525Профессионально реализуем интернет проекты любой '
                                       'технической оснащенности и конфигурации, ведя разработку с учетом SEO.\n'
                                       '\U00002714У нас в штате сертифицированные веб-программисты и '
                                       'мы используем современные технологии.', reply_markup=keyb.choice_1_1_site())

        # level 3 - from on_key - mob_app
        elif call.data == 'mob_app':
            bot.send_message(message.chat.id, 'Опишите свой проект в двух словах')
            msg = 'И затем, оставьте свой номер для связи по кнопке низу экрана.'
            bot.send_message(message.chat.id, msg, reply_markup=keyb.send_phone_keyboard())

            @bot.message_handler(content_types=['text'])
            def await_text(message):
                a = message.text

                @bot.message_handler(content_types=['contact'])
                def contact(message):
                    id = 'Под ключ -> Мобильное приложение'
                    data = {
                        'phone': message.contact.phone_number,
                        'user_name': message.contact.first_name,
                        'call': id
                    }
                    if mailing.send_mail(data=data, text=a):
                        bot.answer_callback_query(call.id, show_alert=True, text="Ваша заявка успешно отправлена!")
                        bot.send_message(message.chat.id, 'Ваша заявка успешно отправлена!\n '
                                                          'Мы обязательно с Вами свяжемся в ближайшее время!',
                                         reply_markup=keyb.hello_keyboard())
                    else:
                        bot.send_message(message.chat.id, 'Упс, что-то пошло не так!',
                                         reply_markup=keyb.hello_keyboard())

        # level 3 - from on_key - all
        elif call.data == 'all':
            bot.send_message(message.chat.id, 'Опишите свой проект в двух словах')
            msg = 'И затем, оставьте свой номер для связи по кнопке низу экрана.'
            bot.send_message(message.chat.id, msg, reply_markup=keyb.send_phone_keyboard())

            @bot.message_handler(content_types=['text'])
            def await_text(message):
                a = message.text

                @bot.message_handler(content_types=['contact'])
                def contact(message):
                    id = 'Под ключ -> И то и то'
                    data = {
                        'phone': message.contact.phone_number,
                        'user_name': message.contact.first_name,
                        'call': id
                    }
                    if mailing.send_mail(data=data, text=a):
                        bot.answer_callback_query(call.id, show_alert=True, text="Ваша заявка успешно отправлена!")
                        bot.send_message(message.chat.id, 'Ваша заявка успешно отправлена!\n'
                                                          'Мы обязательно с Вами свяжемся в ближайшее время!',
                                         reply_markup=keyb.hello_keyboard())
                    else:
                        bot.send_message(message.chat.id, 'Упс, что-то пошло не так!',
                                         reply_markup=keyb.hello_keyboard())

        ###################
        #
        # level 3 point 2 - Дизайн/Редизайн
        # level 3 - from design/redesign - New design
        elif call.data == 'new_design':
            msg = 'Оставьте свой номер для связи.'
            bot.send_message(message.chat.id, msg, reply_markup=keyb.send_phone_keyboard())

            @bot.message_handler(content_types=['contact'])
            def contact(message):
                id = 'Дизайн -> Новый дизайн'
                data = {
                    'phone': message.contact.phone_number,
                    'user_name': message.contact.first_name,
                    'call': id
                }
                if mailing.send_mail(data=data):
                    bot.answer_callback_query(call.id, show_alert=True, text="Ваша заявка успешно отправлена!")
                    bot.send_message(message.chat.id, 'Ваша заявка успешно отправлена!\n'
                                                      'Мы обязательно с Вами свяжемся в ближайшее время!',
                                     reply_markup=keyb.hello_keyboard())
                else:
                    bot.send_message(message.chat.id, 'Упс, что-то пошло не так!', reply_markup=keyb.hello_keyboard())

        # level 3 - from design/redesign - old design
        elif call.data == 'old_design':
            msg = 'Оставьте свой номер для связи.'
            bot.send_message(message.chat.id, msg, reply_markup=keyb.send_phone_keyboard())

            @bot.message_handler(content_types=['contact'])
            def contact(message):
                id = 'Дизайн -> Доработка дизайна текущего'
                data = {
                    'phone': message.contact.phone_number,
                    'user_name': message.contact.first_name,
                    'call': id
                }
                if mailing.send_mail(data=data):
                    bot.answer_callback_query(call.id, show_alert=True, text="Ваша заявка успешно отправлена!")
                    bot.send_message(message.chat.id, 'Ваша заявка успешно отправлена!\n'
                                                      'Мы обязательно с Вами свяжемся в ближайшее время!',
                                     reply_markup=keyb.hello_keyboard())
                else:
                    bot.send_message(message.chat.id, 'Упс, что-то пошло не так!', reply_markup=keyb.hello_keyboard())

        # level 3 - from design/redesign - consultation
        elif call.data == 'cons12':
            msg = 'Оставьте свой номер для связи.'
            bot.send_message(message.chat.id, msg, reply_markup=keyb.send_phone_keyboard())

            @bot.message_handler(content_types=['contact'])
            def contact(message):
                id = 'Дизайн -> Консультация'
                data = {
                    'phone': message.contact.phone_number,
                    'user_name': message.contact.first_name,
                    'call': id
                }
                if mailing.send_mail(data=data):
                    bot.answer_callback_query(call.id, show_alert=True, text="Ваша заявка успешно отправлена!")
                    bot.send_message(message.chat.id, 'Ваша заявка успешно отправлена!\n'
                                                      'Мы обязательно с Вами свяжемся в ближайшее время!',
                                     reply_markup=keyb.hello_keyboard())
                else:
                    bot.send_message(message.chat.id, 'Упс, что-то пошло не так!', reply_markup=keyb.hello_keyboard())

        ###################
        #
        # level 3 point 3 - Доработка/Поддержка
        # level 3 - from support - consultation
        elif call.data == 'refactoring':
            msg = 'Оставьте свой номер для связи.'
            bot.send_message(message.chat.id, msg, reply_markup=keyb.send_phone_keyboard())

            @bot.message_handler(content_types=['contact'])
            def contact(message):
                id = 'Доработка/Поддержка -> Разовые доработки'
                data = {
                    'phone': message.contact.phone_number,
                    'user_name': message.contact.first_name,
                    'call': id
                }
                if mailing.send_mail(data=data):
                    bot.answer_callback_query(call.id, show_alert=True, text="Ваша заявка успешно отправлена!")
                    bot.send_message(message.chat.id, 'Ваша заявка успешно отправлена!\n'
                                                      'Мы обязательно с Вами свяжемся в ближайшее время!',
                                     reply_markup=keyb.hello_keyboard())
                else:
                    bot.send_message(message.chat.id, 'Упс, что-то пошло не так!', reply_markup=keyb.hello_keyboard())

        # level 3 - from support - tech_support
        elif call.data == 'tech_support':
            msg = 'Оставьте свой номер для связи.'
            bot.send_message(message.chat.id, msg, reply_markup=keyb.send_phone_keyboard())

            @bot.message_handler(content_types=['contact'])
            def contact(message):
                id = 'Доработка/Поддержка -> Тех.поддержка'
                data = {
                    'phone': message.contact.phone_number,
                    'user_name': message.contact.first_name,
                    'call': id
                }
                if mailing.send_mail(data=data):
                    bot.answer_callback_query(call.id, show_alert=True, text="Ваша заявка успешно отправлена!")
                    bot.send_message(message.chat.id, 'Ваша заявка успешно отправлена!\n'
                                                      'Мы обязательно с Вами свяжемся в ближайшее время!',
                                     reply_markup=keyb.hello_keyboard())
                else:
                    bot.send_message(message.chat.id, 'Упс, что-то пошло не так!',
                                     reply_markup=keyb.hello_keyboard())

        # level 3 - from support - integration
        elif call.data == 'integration':
            msg = 'Оставьте свой номер для связи.'
            bot.send_message(message.chat.id, msg, reply_markup=keyb.send_phone_keyboard())

            @bot.message_handler(content_types=['contact'])
            def contact(message):
                id = 'Доработка/Поддержка -> Интеграция 1С'
                data = {
                    'phone': message.contact.phone_number,
                    'user_name': message.contact.first_name,
                    'call': id
                }
                if mailing.send_mail(data=data):
                    bot.answer_callback_query(call.id, show_alert=True, text="Ваша заявка успешно отправлена!")
                    bot.send_message(message.chat.id, 'Ваша заявка успешно отправлена!\n'
                                                      'Мы обязательно с Вами свяжемся в ближайшее время!',
                                     reply_markup=keyb.hello_keyboard())
                else:
                    bot.send_message(message.chat.id, 'Упс, что-то пошло не так!',
                                     reply_markup=keyb.hello_keyboard())

        # level 3 - from support - payment
        elif call.data == 'payment':
            msg = 'Оставьте свой номер для связи.'
            bot.send_message(message.chat.id, msg, reply_markup=keyb.send_phone_keyboard())

            @bot.message_handler(content_types=['contact'])
            def contact(message):
                id = 'Доработка/Поддержка -> Платежные системы'
                data = {
                    'phone': message.contact.phone_number,
                    'user_name': message.contact.first_name,
                    'call': id
                }
                if mailing.send_mail(data=data):
                    bot.answer_callback_query(call.id, show_alert=True, text="Ваша заявка успешно отправлена!")
                    bot.send_message(message.chat.id, 'Ваша заявка успешно отправлена!\n'
                                                      'Мы обязательно с Вами свяжемся в ближайшее время!',
                                     reply_markup=keyb.hello_keyboard())
                else:
                    bot.send_message(message.chat.id, 'Упс, что-то пошло не так!',
                                     reply_markup=keyb.hello_keyboard())

        # level 3 - from support - cons13
        elif call.data == 'cons13':
            msg = 'Оставьте свой номер для связи.'
            bot.send_message(message.chat.id, msg, reply_markup=keyb.send_phone_keyboard())

            @bot.message_handler(content_types=['contact'])
            def contact(message):
                id = 'Доработка/Поддержка -> Консультация'
                data = {
                    'phone': message.contact.phone_number,
                    'user_name': message.contact.first_name,
                    'call': id
                }
                if mailing.send_mail(data=data):
                    bot.answer_callback_query(call.id, show_alert=True, text="Ваша заявка успешно отправлена!")
                    bot.send_message(message.chat.id, 'Ваша заявка успешно отправлена!\n'
                                                      'Мы обязательно с Вами свяжемся в ближайшее время!',
                                     reply_markup=keyb.hello_keyboard())
                else:
                    bot.send_message(message.chat.id, 'Упс, что-то пошло не так!',
                                     reply_markup=keyb.hello_keyboard())

        ###################
        #
        # level 3 point 4 - Продвижение/Продвижение
        # level 3 from optimization - search
        elif call.data == 'search':
            msg = 'Оставьте свой номер для связи.'
            bot.send_message(message.chat.id, msg, reply_markup=keyb.send_phone_keyboard())

            @bot.message_handler(content_types=['contact'])
            def contact(message):
                id = 'Продвижение/Продвижение -> Продвижение в поиске'
                data = {
                    'phone': message.contact.phone_number,
                    'user_name': message.contact.first_name,
                    'call': id
                }
                if mailing.send_mail(data=data):
                    bot.answer_callback_query(call.id, show_alert=True, text="Ваша заявка успешно отправлена!")
                    bot.send_message(message.chat.id, 'Ваша заявка успешно отправлена!\n'
                                                      'Мы обязательно с Вами свяжемся в ближайшее время!',
                                     reply_markup=keyb.hello_keyboard())
                else:
                    bot.send_message(message.chat.id, 'Упс, что-то пошло не так!',
                                     reply_markup=keyb.hello_keyboard())

        # level 3 from optimization - seo
        elif call.data == 'seo':
            msg = 'Оставьте свой номер для связи.'
            bot.send_message(message.chat.id, msg, reply_markup=keyb.send_phone_keyboard())

            @bot.message_handler(content_types=['contact'])
            def contact(message):
                id = 'Продвижение/Продвижение -> Разовая SEO'
                data = {
                    'phone': message.contact.phone_number,
                    'user_name': message.contact.first_name,
                    'call': id
                }
                if mailing.send_mail(data=data):
                    bot.answer_callback_query(call.id, show_alert=True, text="Ваша заявка успешно отправлена!")
                    bot.send_message(message.chat.id, 'Ваша заявка успешно отправлена!'
                                                      '\nМы обязательно с Вами свяжемся в ближайшее время!',
                                     reply_markup=keyb.hello_keyboard())
                else:
                    bot.send_message(message.chat.id, 'Упс, что-то пошло не так!',
                                     reply_markup=keyb.hello_keyboard())

        # level 3 from optimization - cons14
        elif call.data == 'cons14':
            msg = 'Оставьте свой номер для связи.'
            bot.send_message(message.chat.id, msg, reply_markup=keyb.send_phone_keyboard())

            @bot.message_handler(content_types=['contact'])
            def contact(message):
                id = 'Продвижение/Продвижение -> Консультация'
                data = {
                    'phone': message.contact.phone_number,
                    'user_name': message.contact.first_name,
                    'call': id
                }
                if mailing.send_mail(data=data):
                    bot.answer_callback_query(call.id, show_alert=True, text="Ваша заявка успешно отправлена!")
                    bot.send_message(message.chat.id, 'Ваша заявка успешно отправлена!'
                                                      '\nМы обязательно с Вами свяжемся в ближайшее время!',
                                     reply_markup=keyb.hello_keyboard())
                else:
                    bot.send_message(message.chat.id, 'Упс, что-то пошло не так!',
                                     reply_markup=keyb.hello_keyboard())

        ###################
        #
        # level 3 point 5 - Реклама
        # level 3 - from adver - yandex
        elif call.data == 'yandex':
            msg = 'Оставьте свой номер для связи.'
            bot.send_message(message.chat.id, msg, reply_markup=keyb.send_phone_keyboard())

            @bot.message_handler(content_types=['contact'])
            def contact(message):
                id = 'Реклама -> Яндекс.Директ'
                data = {
                    'phone': message.contact.phone_number,
                    'user_name': message.contact.first_name,
                    'call': id
                }
                if mailing.send_mail(data=data):
                    bot.answer_callback_query(call.id, show_alert=True, text="Ваша заявка успешно отправлена!")
                    bot.send_message(message.chat.id, 'Ваша заявка успешно отправлена!'
                                                      '\nМы обязательно с Вами свяжемся в ближайшее время!',
                                     reply_markup=keyb.hello_keyboard())
                else:
                    bot.send_message(message.chat.id, 'Упс, что-то пошло не так!', reply_markup=keyb.hello_keyboard())

        # level 3 - from adver - google
        elif call.data == 'google':
            msg = 'Оставьте свой номер для связи.'
            bot.send_message(message.chat.id, msg, reply_markup=keyb.send_phone_keyboard())

            @bot.message_handler(content_types=['contact'])
            def contact(message):
                id = 'Реклама -> Google Ad'
                data = {
                    'phone': message.contact.phone_number,
                    'user_name': message.contact.first_name,
                    'call': id
                }
                if mailing.send_mail(data=data):
                    bot.answer_callback_query(call.id, show_alert=True, text="Ваша заявка успешно отправлена!")
                    bot.send_message(message.chat.id, 'Ваша заявка успешно отправлена!'
                                                      '\nМы обязательно с Вами свяжемся в ближайшее время!',
                                     reply_markup=keyb.hello_keyboard())
                else:
                    bot.send_message(message.chat.id, 'Упс, что-то пошло не так!', reply_markup=keyb.hello_keyboard())

        # level 3 - from adver - smm
        elif call.data == 'smm':
            msg = 'Оставьте свой номер для связи.'
            bot.send_message(message.chat.id, msg, reply_markup=keyb.send_phone_keyboard())

            @bot.message_handler(content_types=['contact'])
            def contact(message):
                id = 'Реклама -> SMM'
                data = {
                    'phone': message.contact.phone_number,
                    'user_name': message.contact.first_name,
                    'call': id
                }
                if mailing.send_mail(data=data):
                    bot.answer_callback_query(call.id, show_alert=True, text="Ваша заявка успешно отправлена!")
                    bot.send_message(message.chat.id, 'Ваша заявка успешно отправлена!'
                                                      '\nМы обязательно с Вами свяжемся в ближайшее время!',
                                     reply_markup=keyb.hello_keyboard())
                else:
                    bot.send_message(message.chat.id, 'Упс, что-то пошло не так!', reply_markup=keyb.hello_keyboard())

        # level 3 - from adver - all15
        elif call.data == 'all15':
            msg = 'Оставьте свой номер для связи.'
            bot.send_message(message.chat.id, msg, reply_markup=keyb.send_phone_keyboard())

            @bot.message_handler(content_types=['contact'])
            def contact(message):
                id = 'Реклама -> Нужно все'
                data = {
                    'phone': message.contact.phone_number,
                    'user_name': message.contact.first_name,
                    'call': id
                }
                if mailing.send_mail(data=data):
                    bot.answer_callback_query(call.id, show_alert=True, text="Ваша заявка успешно отправлена!")
                    bot.send_message(message.chat.id, 'Ваша заявка успешно отправлена!'
                                                      '\nМы обязательно с Вами свяжемся в ближайшее время!',
                                     reply_markup=keyb.hello_keyboard())
                else:
                    bot.send_message(message.chat.id, 'Упс, что-то пошло не так!', reply_markup=keyb.hello_keyboard())

        # level 3 - from adver - cons15
        elif call.data == 'cons15':
            msg = 'Оставьте свой номер для связи.'
            bot.send_message(message.chat.id, msg, reply_markup=keyb.send_phone_keyboard())

            @bot.message_handler(content_types=['contact'])
            def contact(message):
                id = 'Реклама -> Кнсультация'
                data = {
                    'phone': message.contact.phone_number,
                    'user_name': message.contact.first_name,
                    'call': id
                }
                if mailing.send_mail(data=data):
                    bot.answer_callback_query(call.id, show_alert=True, text="Ваша заявка успешно отправлена!")
                    bot.send_message(message.chat.id, 'Ваша заявка успешно отправлена!'
                                                      '\nМы обязательно с Вами свяжемся в ближайшее время!',
                                     reply_markup=keyb.hello_keyboard())
                else:
                    bot.send_message(message.chat.id, 'Упс, что-то пошло не так!', reply_markup=keyb.hello_keyboard())

        ######################################
        #
        # level 4  - Сайт
        # level 4 - from site - company
        elif call.data == 'company':
            bot.send_message(message.chat.id, 'Опишите свой проект в двух словах')
            msg = 'И затем, оставьте свой номер для связи по кнопке низу экрана.'
            bot.send_message(message.chat.id, msg, reply_markup=keyb.send_phone_keyboard())

            @bot.message_handler(content_types=['text'])
            def await_text(message):
                a = message.text

                @bot.message_handler(content_types=['contact'])
                def contact(message):
                    id = 'Под ключ -> Сайт -> Сайт компании'
                    data = {
                        'phone': message.contact.phone_number,
                        'user_name': message.contact.first_name,
                        'call': id
                    }
                    if mailing.send_mail(data=data, text=a):
                        bot.answer_callback_query(call.id, show_alert=True, text="Ваша заявка успешно отправлена!")
                        bot.send_message(message.chat.id, 'Ваша заявка успешно отправлена!'
                                                          '\nМы обязательно с Вами свяжемся в ближайшее время!',
                                         reply_markup=keyb.hello_keyboard())
                    else:
                        bot.send_message(message.chat.id, 'Упс, что-то пошло не так!', reply_markup=keyb.hello_keyboard())

        # level 4 - from site - eshop
        elif call.data == 'eshop':
            bot.send_message(message.chat.id, 'Опишите свой проект в двух словах')
            msg = 'И затем, оставьте свой номер для связи по кнопке низу экрана.'
            bot.send_message(message.chat.id, msg, reply_markup=keyb.send_phone_keyboard())

            @bot.message_handler(content_types=['text'])
            def await_text(message):
                a = message.text

                @bot.message_handler(content_types=['contact'])
                def contact(message):
                    id = 'Под ключ -> Сайт -> Интернет магазин'
                    data = {
                        'phone': message.contact.phone_number,
                        'user_name': message.contact.first_name,
                        'call': id
                    }
                    if mailing.send_mail(data=data, text=a):
                        bot.answer_callback_query(call.id, show_alert=True, text="Ваша заявка успешно отправлена!")
                        bot.send_message(message.chat.id, 'Ваша заявка успешно отправлена!'
                                                          '\nМы обязательно с Вами свяжемся в ближайшее время!',
                                         reply_markup=keyb.hello_keyboard())
                    else:
                        bot.send_message(message.chat.id, 'Упс, что-то пошло не так!', reply_markup=keyb.hello_keyboard())

        # level 4 - from site - info
        elif call.data == 'info':
            bot.send_message(message.chat.id, 'Опишите свой проект в двух словах')
            msg = 'И затем, оставьте свой номер для связи по кнопке низу экрана.'
            bot.send_message(message.chat.id, msg, reply_markup=keyb.send_phone_keyboard())

            @bot.message_handler(content_types=['text'])
            def await_text(message):
                a = message.text

                @bot.message_handler(content_types=['contact'])
                def contact(message):
                    id = 'Под ключ -> Сайт -> Информационный сайт'
                    data = {
                        'phone': message.contact.phone_number,
                        'user_name': message.contact.first_name,
                        'call': id
                    }
                    if mailing.send_mail(data=data, text=a):
                        bot.answer_callback_query(call.id, show_alert=True, text="Ваша заявка успешно отправлена!")
                        bot.send_message(message.chat.id, 'Ваша заявка успешно отправлена!\n'
                                                          'Мы обязательно с Вами свяжемся в ближайшее время!',
                                         reply_markup=keyb.hello_keyboard())
                    else:
                        bot.send_message(message.chat.id, 'Упс, что-то пошло не так!', reply_markup=keyb.hello_keyboard())

        # level 4 - from site - lending
        elif call.data == 'lending':
            bot.send_message(message.chat.id, 'Опишите свой проект в двух словах')
            msg = 'И затем, оставьте свой номер для связи по кнопке низу экрана.'
            bot.send_message(message.chat.id, msg, reply_markup=keyb.send_phone_keyboard())

            @bot.message_handler(content_types=['text'])
            def await_text(message):
                a = message.text

                @bot.message_handler(content_types=['contact'])
                def contact(message):
                    id = 'Под ключ -> Сайт -> Лендинг'
                    data = {
                        'phone': message.contact.phone_number,
                        'user_name': message.contact.first_name,
                        'call': id
                    }
                    if mailing.send_mail(data=data, text=a):
                        bot.answer_callback_query(call.id, show_alert=True, text="Ваша заявка успешно отправлена!")
                        bot.send_message(message.chat.id, 'Ваша заявка успешно отправлена!\n'
                                                          'Мы обязательно с Вами свяжемся в ближайшее время!',
                                         reply_markup=keyb.hello_keyboard())
                    else:
                        bot.send_message(message.chat.id, 'Упс, что-то пошло не так!', reply_markup=keyb.hello_keyboard())


if __name__ == '__main__':
    Thread(target=bot.infinity_polling, args=(True,)).start()

