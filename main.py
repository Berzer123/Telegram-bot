from multiprocessing import get_context
import telebot
from telebot import types
import random
from multiprocessing.sharedctypes import Value
from pprint import pprint
from tokenize import Name
import requests





TOKEN = '5320585857:AAGp71Q5r4EPf6w9KfYc4YyXbMTnsDpzQ64'

bot = telebot.TeleBot(TOKEN)

url_crb = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()    # запрос json файла в црб
# usd = pprint(data['Valute']['USD'])
# for i in usd:
#     print(i)
def get_usd(url_crb):
    list_data = []
    usd = url_crb['Valute']['USD']
    list = usd.values()
    for i in list:
        list_data.append(i)
    return list_data[-2]


def get_eur(url_crb):
    list_data = []
    usd = url_crb['Valute']['EUR']
    list = usd.values()
    for i in list:
        list_data.append(i)
    return list_data[-2]

usd = get_usd(url_crb)
eur = get_eur(url_crb)

def decimal_to_binary(x):
    try:
        return bin(int(x))
    except:
        return 'Цифры ударили мне в голову. А ты не можешь попасть пальцами по цифоркам, алкаш!!!'


def binary_to_decimal(x):   # перевод из двоичной в 10-ную систему счислений
    try:
        return int(x, 2)
    except:
        return 'В двоичном коде могут быть только 1 и 0 :('


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard= True)
    item1 = types.KeyboardButton('Рандомное число')
    item2 = types.KeyboardButton('Курсы валют')
    item3 = types.KeyboardButton('Перевод из 10-ной системы, в двоичную')
    item4 = types.KeyboardButton('Перевод из 2-ичной системы, в 10-ную')

    markup.add(item1, item2, item3, item4)

    bot.send_message(message.chat.id, 'Привет, {0.first_name}!'.format(message.from_user), reply_markup = markup)

@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == 'Рандомное число':
            bot.send_message(message.chat.id, 'Ваши число: ' + str(random.randint(0, 1000)))
        elif message.text == 'Курсы валют':
            bot.send_message(message.chat.id, 'Курс Доллара: ' f"{usd}")
            bot.send_message(message.chat.id, 'Курс Евро: ' f"{eur}")
        elif message.text == 'Перевод из 10-ной системы, в двоичную':
            sent = bot.send_message(message.from_user.id, "Введите число: ")
            bot.register_next_step_handler(sent, get_context)
        elif message.text == 'Перевод из 2-ичной системы, в 10-ную':
            binary = bot.send_message(message.from_user.id, "Введите число: ")
            bot.register_next_step_handler(binary, get_context1)

def get_context(message):   # вот эта функция возвращает текст из десятичной в двоичную
    name = message.text
    print(name)
    b = decimal_to_binary(name)
    bot.send_message(message.from_user.id, b[2:])
    print(b)


def get_context1(message):   # вот эта поебень должна вернуть из двоичной в десятичную 
    name = message.text
    print(name)
    b = binary_to_decimal(name)
    bot.send_message(message.from_user.id, b)
    print(b)





bot.polling(none_stop = True)