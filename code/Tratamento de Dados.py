import pymongo as pm

tweets = pm.MongoClient().ColetaEleicoes.tweets
output = open("Resultado.txt", 'w', encoding="utf8")

UL = [] # UL = Lista de todos os users mencionados
UA = [] # UA = Lista de users já analisados
contagem = 0

for tweet in tweets.find():
    user = str.lower(tweet["user"]["screen_name"])
    UL.append(user)

for user in UL:
    if user not in UA:
        contagem = UL.count(user)
        if contagem > 25:
            output.writelines("@" + str(user) +" " + str(contagem)+"\n")
        UA.append(user)
        contagem = 0

output.close