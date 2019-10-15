from time import sleep
from html import escape
from configparser import ConfigParser

import requests
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from plugin import db_tools

config = ConfigParser()
config.read('config.txt')
master = config.getint('admin', 'master')
red = db_tools.use_redis()
group = -1001418862434


class famimart:
    def event(self, content):
        self.img = content['img']
        self.date = content['date']
        self.title = content['title']
        self.desc = content['description']
        self.link = content['link']

    def new_goods(self, content):
        self.img = content['Img']
        self.title = content['Title']
        self.date = content['Dates']
        self.event_start = content['EventStart']
        self.event_end = content['EventEnd']
        self.desc = content['Content']
        self.link = content['Link']
        self.price = content['Price']


def checker(url: 'string'):
    tmp = red.lrange('famievent', 0, -1)
    if url.encode() in tmp:
        return True
    else:
        return False


def event(bot, update):
    r = requests.get('https://www.family.com.tw/mobile/api/eventjson.ashx')
    if r.status_code != 200:
        bot.send_message(master, 'FamiEvent HTTP/Get Error')
        return
    try:
        content = r.json()
    except:
        bot.send_message(master, 'FamiEvent de_json Error')
    for fami_type in content:
        for fami_content in content[fami_type]:
            # img, date, title, description, link
            # date = fami_content['date']
            # title = fami_content['title']
            # desc = fami_content['description']
            # link = fami_content['link']
            fami = famimart()
            fami.event(fami_content)
            '''
            [最新活動]
            *輕食生活誌*
            個人化全家服務超便利！
            [button]
            '''
            duplicate = checker(fami.img)
            if duplicate:
                return
            red.lpush('famievent', fami.img)
            text = '<b>[最新活動]</b>\n' \
                f'{escape(fami.title)}\n' \
                f'簡述：{escape(fami.desc)}\n' \
                f'期間：{fami.date}'
            button = InlineKeyboardMarkup(
                [[InlineKeyboardButton('點我前往', url=fami.link.replace(' ', ''))]])
            try:
                bot.send_message(group, text,
                                 reply_markup=button, parse_mode='html', disable_web_page_preview=True)
            except:
                bot.send_message(group, text, parse_mode='html',
                                 disable_web_page_preview=True)


def new_goods(bot, update):
    r = requests.get('https://www.family.com.tw/mobile/api/ProductJson.ashx')
    if r.status_code != 200:
        bot.send_message(master, 'FamiNewGoods HTTP/Get Error')
        return
    try:
        content = r.json()
    except:
        bot.send_message(master, 'FamiNewGoods de_json Error')

    all_category = content['EventNewOrder']
    for category in all_category:
        if content[category]:
            for items in content[category]:
                fami = famimart()
                fami.new_goods(items)
                duplicate = checker(fami.img)
                if duplicate:
                    return
                '''
                [新品情報]
                啤酒好好好 49$
                夏天就是要喝酒配ㄓㄊ，不然要幹嘛？
                '''
                new_line = '\n'
                red.lpush('famievent', fami.img)
                text = '<b>[新品情報]</b>\n' \
                    f'{escape(fami.title)} <code>{fami.price}$</code>\n' \
                    f'{escape(fami.desc)}\n' \
                    f"{f'時間：{fami.date}{new_line}' if fami.date else ''}" \
                    f"{f'活動期間：{fami.event_start} ~ {fami.event_end}{new_line}' if fami.event_start else ''}"
                button = InlineKeyboardMarkup(
                    [[InlineKeyboardButton('點我前往', url=fami.link)]])
                if fami.link:
                    bot.send_message(group, text,
                                     reply_markup=button, parse_mode='html', disable_web_page_preview=True)
                else:
                    bot.send_message(group, text, parse_mode='html',
                                     disable_web_page_preview=True)
                sleep(5)
