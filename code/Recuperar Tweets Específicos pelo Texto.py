import pymongo as pm

tweets = pm.MongoClient().ColetaEleicoes.tweets

arquivo = open("Output/Santo André - Paulo Serra.txt", 'w', encoding="utf8")

for tweet in tweets.find():
    bruto = str.lower(tweet["text"])
    textoi = bruto.split()
    texto = " ".join(textoi)
    if "paulo serra" in texto:
            arquivo.writelines(texto + "\n")

arquivo.close

# =========================================================#

arquivo = open("Output/São Caetano do Sul - Paulo Pinheiro.txt", 'w', encoding="utf8")

for tweet in tweets.find():
    bruto = str.lower(tweet["text"])
    textoi = bruto.split()
    texto = " ".join(textoi)
    if "paulo pinheiro" in texto:
        arquivo.writelines(texto + "\n")

arquivo.close
