from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from . import bot, logging, info #log,


@dataclass_json
@dataclass
class Configure:
    """
    設定檔類型
    """
    bot: bot = bot.Bot
    # log: log = field(hash=False, repr=True, compare=False, default=None)
    info: info = field(hash=False, repr=True, compare=False, default=None)
    logging: logging = logging.Logging
    mongo: str = field(hash=False, repr=True, compare=False, default=None)

