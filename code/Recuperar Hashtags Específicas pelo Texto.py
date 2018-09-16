import pymongo as pm

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

tweets = pm.MongoClient().ColetaEleicoes.tweets
arquivo = open("Filtragem - hashtags kiko.txt", 'w', encoding="utf8")

HTL = [] # HTL = Lista de todas as hashtags usadas
HTA = [] # HTA = Lista de hashtags já analisadas

for tweet in tweets.find():
    texto = str.lower(tweet["text"])
    if "grecco" in texto:
        for h in tweet["entities"]["hashtags"]:
            hashtag = str.lower(h["text"])
            hashtag = desacentuar(hashtag)
            HTL.append(hashtag)

for hash in HTL:
    if hash not in HTA:
        contagem = HTL.count(hash)
        arquivo.writelines("#" + str(hash) +" " + str(contagem))
        arquivo.writelines("\n")
        HTA.append(hash)
        contagem = 0

arquivo.close
