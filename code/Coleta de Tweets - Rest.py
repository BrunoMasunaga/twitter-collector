from twython import Twython
import pymongo as pm
import time

apk = "insert apk"
aps = "insert aps"
oat = "insert oat"
ots = "insert ots"
twitter = Twython(apk, aps, oat, ots)
tweets = pm.MongoClient().ColetaLulaRecuperar.tweets

assuntos = []

coleta = twitter.search(q = assuntos, count = 100)
tweets.insert(coleta["statuses"])

oldest = coleta["statuses"][-1]["id_str"]
oldest = int(oldest) - 1

while (True):
    coleta = twitter.search(q = assuntos, count = 100, max_id = oldest)
    tweets.insert(coleta["statuses"])
    oldest = coleta["statuses"][-1]["id_str"]
    oldest = int(oldest) - 1
    time.sleep(2)
