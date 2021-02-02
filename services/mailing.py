import smtplib, ssl
from loguru import logger
import settings

logger.add("log/log.json", level="DEBUG", format="{time} {level} {message}", serialize=True,
           rotation="1 MB", compression="zip")


@logger.catch()
def send_mail(data, text=None):
    """
    Функция отправки сообщение с данными о заявки от заказчика
    :param text:
    :param data: {'name': <>, 'email': <>, 'subject': <>}
    :return: True or False with error text
    """

    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = settings.EMAIL  # Enter your address
    receiver_email = settings.EMAIL  # Enter receiver address
    password = settings.PASSW
    if text is None:
        message = """
        Subject: Заявка по: {}'
        
        Номер телефона: {}
        Имя заказчика: {}""".format(
            data['call'],
            str(data['phone']),
            str(data['user_name'])
        )
    else:
        message = """
        Subject: Заявка по: {}'

        Номер телефона: {}
        Имя заказчика: {}
        Текст: {}""".format(
            data['call'],
            str(data['phone']),
            str(data['user_name']),
            text
        )

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.encode('utf-8'))

    return True

