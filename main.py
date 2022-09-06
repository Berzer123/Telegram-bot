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

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard= True)
    item1 = types.KeyboardButton('Рандомное число')
    item2 = types.KeyboardButton('Курсы валют')
    item3 = types.KeyboardButton('Информация')
    item4 = types.KeyboardButton('Другое')

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
bot.polling(none_stop = True)