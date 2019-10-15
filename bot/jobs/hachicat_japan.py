import logging
import requests
from pyquery import PyQuery as pq
from dateutil import tz
from datetime import datetime
url = 'http://dorama.info'
timezone = tz.gettz('Asia/Taipei')


def birthday(bot, update):
    r = requests.get(url)
    pquery = pq(r.text)
    now = datetime.today().year

    tmp = str()  # list()

    for x in pquery('.table3_g').items():
        if '今天生日' in x('tr').eq(0).text():
            birthdaylist = list(x('.td_dt_g').items())

    for ages in birthdaylist:
        if ages('td')('a').text():
            url_ = ages('a').attr('href')
            bth_ = pq(requests.get(url+url_).text)
            bth = bth_('.sz1.fcol_cast').eq(0).text().split('\n\n')
            name = ages('a').text()

            for dt in bth:
                if '生\u3000日：\n' in dt:
                    age = now - \
                        int(dt.replace('生\u3000日：\n', '').split('-')[0])
                    if age <= 200:
                        tmp += f'（{age} 才）' + name + '\n'
                    else:
                        tmp += f'（未提供）' + name + '\n'

    dt = datetime.now(timezone)
    tmp = f'{dt.strftime("%m/%d")} 今日日本偶像壽星\n' + tmp

    bot.send_message(-1001350314761, tmp, disable_web_page_preview=True)
