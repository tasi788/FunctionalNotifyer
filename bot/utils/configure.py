import os
import sys
import yaml

from ..types import utils


def loads():
    if os.path.isfile('config.yml'):
        file = open('config.yml', 'r').read()
    else:
        sys.exit(0)

    # read fileIO to parser
    parser = yaml.safe_load(file)

    # make dataclass
    return utils.Configure.from_dict(parser)