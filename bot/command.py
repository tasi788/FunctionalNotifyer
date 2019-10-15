import re
import sys
import time
import logging
import threading
from html import escape
from pprint import pprint as pp
from datetime import datetime, timedelta
from dateutil import tz

import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext.dispatcher import run_async
from telegram.error import *


class app:
    '''
    db rule

    hexlightning.chat_action.json
    '''

    def __init__(self, inherit):
        logger = logging.getLogger(__name__)
        self.logger = inherit.logger
        self.config = inherit.config

    def ta(self, bot, update):
        # update.message.reply_text('pong')
        # pp(update.message.to_dict())
        bot.send_message(525239263, 'hi')
        print('ho')

    def error(self, bot, update, error):
        self.logger.warning('Update "%s" caused error "%s"', update, error)
