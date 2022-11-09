from notifiers import get_notifier
from lolzapi import LolzteamApi
from time import sleep

chatId = 912957048
token = '5320585857:AAGp71Q5r4EPf6w9KfYc4YyXbMTnsDpzQ64'
api = LolzteamApi('e774ddd4d6c893317126ea84a82a744d7562816e')

telegram = get_notifier('telegram')
telegram.notify(token=token, chat_id=chatId, message='бот запущен')    #отправка сообщения

dictt = {
    'daybreak': '15',
    'mm_ban': 'nomatter',
    'd2_game_count_min': '500',
    'd2_behavior_min': '7000'

}
max_price = 300     # максимальная цена товара
data = []   # для вывода одного товара только один раз
while 1:
    items = api.market_list('steam', pmax=max_price, optional=dictt)
    for i in items['items']:
        # api.market_buy(i['item_id'])
        # print(i)    # храним фулл данные акков
        list_temp = []
        account_id = i['item_id']
        link = 'zelenka.guru/market/' + str(account_id)
        mmr = i["steam_dota2_solo_mmr"]
        behavior = i["steam_dota2_behavior"]
        price = i["price"]
        title = i['title']
        list_temp = [title, price, link, mmr, behavior]
        text_ = f'''Название: {title} \nЦена: {price} \nссылка на товар: {link} \nMmr: {mmr} \nBehavior: {behavior}'''
        if list_temp not in data:
            telegram.notify(token=token, chat_id=chatId, message=text_)  # отправка сообщения
            data.append(list_temp)

    sleep(10)