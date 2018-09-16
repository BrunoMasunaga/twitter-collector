import pymongo as pm


tweets = pm.MongoClient().ColetaEleicoes.tweets
arquivo = open("Filtragem - users kiko.txt", 'w', encoding="utf8")

UL = [] # UL = Lista de todos os users
UA = [] # UA = Lista de users já analisados

for tweet in tweets.find():
    texto = str.lower(tweet["text"])
    if "kiko" in texto:
        user = str.lower(tweet["user"]["screen_name"])
        UL.append(user)

for u in UL:
    if u not in UA:
        contagem = UL.count(u)
        arquivo.writelines("@" + str(u) +" " + str(contagem))
        arquivo.writelines("\n")
        UA.append(u)
        contagem = 0

arquivo.close
