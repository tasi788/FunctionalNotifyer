import logging
import coloredlogs
from time import sleep
from html import escape
from configparser import ConfigParser

import requests
from pyquery import PyQuery as pq
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from plugin import db_tools

logger = logging.getLogger(__name__)
coloredlogs.install('INFO')

red = db_tools.use_redis()
group = -1001418862434
base_url = 'https://www.hilife.com.tw/'


def checker(url: 'string'):
    tmp = red.lrange('hilife', 0, -1)
    if url.encode() in tmp:
        return True
    else:
        return False


def events(bot, update):
    r = requests.get(base_url + 'events_news.aspx')
    if r.status_code != 200:
        return
    get = pq(r.text)
    for x in get('.infoList')('li').items():
        date = x('strong').text()
        url = x('a').attr('href')
        content = x('a').text()
        if checker(url) == False:
            button = InlineKeyboardMarkup(
                [[InlineKeyboardButton('點我前往', url=url.replace(' ', ''))]])

            text = '[Hi-Life 最新消息]\n' + \
                content + '\n' + \
                f'發佈時間：{date}'
            if url:
                try:
                    bot.send_message(group, text,
                                     reply_markup=button, parse_mode='html', disable_web_page_preview=True)
                except:
                    bot.send_message(group, text, parse_mode='html',
                                     disable_web_page_preview=True)
            else:
                bot.send_message(group, text, parse_mode='html',
                                 disable_web_page_preview=True)
            red.lpush('hilife', url)
            red.ltrim('hilife', 0, 100)
