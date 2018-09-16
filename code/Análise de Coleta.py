import pymongo as pm
from stop_words import get_stop_words
from datetime import datetime

LP = [".", ",", ";", ":", "?", "!", "...", "..", "(", ")", "-", "'", '"', "&"] # LEC = Lista de pontuação
tweets = pm.MongoClient().ColetaEleicoes.tweets
contagem = 0

def desacentuar(x):
    x = x.replace("á", "a")
    x = x.replace("à", "a")
    x = x.replace("ã", "a")
    x = x.replace("é", "e")
    x = x.replace("ê", "e")
    x = x.replace("í", "i")
    x = x.replace("ó", "o")
    x = x.replace("ô", "o")
    x = x.replace("õ", "o")
    x = x.replace("ú", "u")
    x = x.replace("ç", "c")
    return x

def despontuar(x):
    for caracter in LP:
        if caracter in x:
            x = x.replace(caracter, "")
    return x

#------------------------------------------------Análise das Hashtags--------------------------------------------------#
print("\n*********ANÁLISE DAS HASHTAGS*********\n")

now = datetime.now()
print ("Local time: " + str(now.hour)+"h "+str(now.minute)+"m "
       +str(now.second)+"s - " +str(now.day)+"/"+str(now.month)+"/"+str(now.year)+"\n")

HTL = [] # HTL = Lista de todas as hashtags usadas
HTA = [] # HTA = Lista de hashtags já analisadas

for tweet in tweets.find():
    for h in tweet["entities"]["hashtags"]:
        hashtag = str.lower(h["text"])
        hashtag = desacentuar(hashtag)
        HTL.append(hashtag)

for hashtag in HTL:
    if hashtag not in HTA:
        contagem = HTL.count(hashtag)
        if contagem > 10:
            print ("#" + str(hashtag) +" " + str(contagem))
        HTA.append(hashtag)
        contagem = 0

#----------------------------------------------------Análise dos Users-------------------------------------------------#
print("\n*********ANÁLISE DOS USERS*********\n")

now = datetime.now()
print ("Local time: " + str(now.hour)+"h "+str(now.minute)+"m "
       +str(now.second)+"s - " +str(now.day)+"/"+str(now.month)+"/"+str(now.year)+"\n")

UL = [] # UL = Lista de todos os users mencionados
UA = [] # UA = Lista de users já analisados

for tweet in tweets.find():
    for h in tweet["entities"]["user_mentions"]:
        user = str.lower(h["screen_name"])
        UL.append(user)

for user in UL:
    if user not in UA:
        contagem = UL.count(user)
        if contagem > 5:
            print ("@" + str(user) +" " + str(contagem))
        UA.append(user)
        contagem = 0

#---------------------------------------------------Análise dos Termos-------------------------------------------------#
print("\n*********ANÁLISE DOS TERMOS*********\n")

now = datetime.now()
print ("Local time: " + str(now.hour)+"h "+str(now.minute)+"m "
       +str(now.second)+"s - " +str(now.day)+"/"+str(now.month)+"/"+str(now.year)+"\n")

gsw = get_stop_words("portuguese") # stop words padrões do português
extra = ["rt"]
stoplist = gsw + extra

TL = [] # TL = Lista de todos os termos usados
TA = [] # TA = Lista de termos já analisados

for tweet in tweets.find():
    texto = str.lower(tweet["text"])
    termos = texto.split()
    for palavra in termos:
        palavra = despontuar(palavra)
        palavra = desacentuar(palavra)
        if palavra not in stoplist and "http" not in palavra and "@" not in palavra and "#" not in palavra and len(palavra) > 3:
            TL.append(palavra)

for palavra in TL:
    if palavra not in TA:
        contagem = TL.count(palavra)
        if contagem > 50:
            print (str(palavra) +" " + str(contagem))
        TA.append(palavra)
        contagem = 0

#------------------------------------------Análise dos Tweets mais retweetados-----------------------------------------#
print("\n*********ANÁLISE DOS TWEETS MAIS RETWEETADOS*********\n")

now = datetime.now()
print ("Local time: " + str(now.hour)+"h "+str(now.minute)+"m "
       +str(now.second)+"s - " +str(now.day)+"/"+str(now.month)+"/"+str(now.year)+"\n")

DR = {} # DR = Dicionário de retweets
DRC = {} # DRC = Dicionário formado por cada retweet

for tweet in tweets.find():
    if "retweeted_status" in tweet:
        id = (tweet["retweeted_status"]["id"])
        contagem = (tweet["retweeted_status"]["retweet_count"])
        if contagem > 10 and id not in DR:

            #text = (tweet["retweeted_status"]["text"])
            #DRC = {str(id): str(str(contagem) + " :::: " + str(text))}

            DRC = {id: contagem}
            DR.update(DRC)
        contagem = 0
print(DR)

#-------------------------------------------Análise dos Tweets mais favoritados----------------------------------------#
print("\n*********ANÁLISE DOS TWEETS MAIS FAVORITADOS*********\n")

now = datetime.now()
print ("Local time: " + str(now.hour)+"h "+str(now.minute)+"m "
       +str(now.second)+"s - " +str(now.day)+"/"+str(now.month)+"/"+str(now.year)+"\n")

DF = {} # DF = Dicionário de favoritados
DFC = {} # DFC = Dicionário formado por cada favoritado

for tweet in tweets.find():
    if "retweeted_status" in tweet:
        id = (tweet["retweeted_status"]["id"])
        contagem = (tweet["retweeted_status"]["favorite_count"])
        if contagem > 10 and id not in DF:

             #text = (tweet["retweeted_status"]["text"])
             #DFC = {str(id): str(str(contagem) + " :::: " + str(text))}

             DFC = {id: contagem}
             DF.update(DFC)
        contagem = 0
print(DF)

#-----------------------------------------------Análise dos Users mais retweetados-------------------------------------#
print("\n*********ANÁLISE DOS USERS MAIS RETWEETADOS*********\n")

now = datetime.now()
print ("Local time: " + str(now.hour)+"h "+str(now.minute)+"m "
       +str(now.second)+"s - " +str(now.day)+"/"+str(now.month)+"/"+str(now.year)+"\n")

URL = [] # URL = Lista de todos os users retweetados
URA = [] # URA = Lista de users já analisados

for tweet in tweets.find():
    if "retweeted_status" in tweet:
        user = str.lower(tweet["retweeted_status"]["user"]["screen_name"])
        URL.append(user)

for user in URL:
    if user not in URA:
        contagem = URL.count(user)
        if contagem > 5:
            print ("@" + str(user) +" " + str(contagem))
        URA.append(user)
        contagem = 0

#--------------------------------------------------Contagem de Retweets------------------------------------------------#
print("\n*********CONTAGEM DE RETWEETS*********\n")

now = datetime.now()
print ("Local time: " + str(now.hour)+"h "+str(now.minute)+"m "
       +str(now.second)+"s - " +str(now.day)+"/"+str(now.month)+"/"+str(now.year)+"\n")

CR = 0 # CR = Contagem de Retweets
CO = 0 # CO = Contagem de Tweets Originais

for tweet in tweets.find():
    if "retweeted_status" in tweet:
        CR += 1
    else:
        CO += 1
print(str(CR) + " retweets.")
print(str(CO) + " tweets originais.")
