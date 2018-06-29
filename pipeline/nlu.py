from postagger import tagger
import os
import json
import logging.config

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '%(levelname)s: %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        '': {
            'level': 'DEBUG',
            'handlers': ['console'],
        },
    },
}
logging.config.dictConfig(LOGGING)

tweetPath = os.path.join(os.getcwd(), "scraper/TweetScraper/TweetScraper/Data/tweet/")
restaurantMenuPath = "/home/basavaraj.r/hadoop/foodie_favorites/data/restaurants.json"

tweets = os.listdir(tweetPath)

"""
for eachTweet in tweets:
	handle = open(os.path.join(tweetPath, eachTweet), 'rb')
	jsstr = handle.read().encode('utf-8')
	tweetMeta  = json.loads(jsstr)
	print tweetMeta["text"]
"""
tp = os.path.join(tweetPath, '754288618999537664')
print(tp)
fhandle = open(tp, 'rb')
jsstr = fhandle.read()
trade = json.loads(jsstr.decode('utf-8'))
print(trade["text"])

pt = tagger.tagger()
pt.configure()
pt.startTraining("tnt")
#print(tagger.tagger.)

"""
rev = open(restaurantMenuPath, 'rb')
jsstr  = rev.read().encode('utf-8')
restMeta = json.loads(jsstr)
text =  (restMeta[0]["info"])
print text
"""
