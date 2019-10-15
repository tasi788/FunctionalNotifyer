import redis
#import pymongo

from configparser import ConfigParser

config = ConfigParser()
config.read('config.txt')


def use_redis():
    return redis.from_url(config.get('db', 'redis'))


def use_mongo():
    #mongo = pymongo.MongoClient(config.get('db', 'mongo'))
    # return mongo
    pass
