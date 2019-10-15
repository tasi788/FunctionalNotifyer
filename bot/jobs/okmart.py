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
base_url = 'https://www.okmart.com.tw/'


def checker(url: 'string'):
    tmp = red.lrange('okmart', 0, -1)
    if url.encode() in tmp:
        return True
    else:
        return False


def promotion1(bot, update):
    r = requests.get(base_url+'promotion_reference')
    if r.status_code != 200:
        return
    get = pq(r.text)
    for x in get('.purchaseList2')('.name2').items():
        url = base_url + x('a').attr('href')
        if checker(url) == False:
            button = InlineKeyboardMarkup(
                [[InlineKeyboardButton('點我前往', url=url.replace(' ', ''))]])
            content = x('a').text()

            text = '[OK 本期特惠]\n' + \
                content
            return
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
            red.lpush('okmart', url)
            red.ltrim('okmart', 0, 100)
