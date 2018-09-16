from twython import TwythonStreamer
import pymongo as pm

class Coleta(TwythonStreamer):
    def __init__(self, apk, aps, oat, ots):
        TwythonStreamer.__init__(self, apk, aps, oat, ots)
        self.tweets = pm.MongoClient().ColetaEleicoes.tweets
        self.users = pm.MongoClient().ColetaEleicoes.users
        self.users.ensure_index("id_str", unique = True)

    def on_success(self, data):
        if "text" in data:
            self.tweets.insert(data)
            self.users.update({"id_str": data["user"]["id_str"]}, {"id_str": data["user"]["id_str"]}, upsert = True)

apk = "insert apk"
aps = "insert aps"
oat = "insert oat"
ots = "insert ots"
stream = Coleta(apk, aps, oat, ots)

"""
assuntos = ["gilma", "Gilma", "impeachment", "Impeachment", "PelaDemocracia",
            "pelaDemocracia", "pelademocracia", "RIPdemocracia", "RIPDemocracia",
            "RipDemocracia", "impeachmentday", "Impeachmentday", "ImpeachmentDay",
            "impeachmentDay", "SomosTodosGolpistas", "somostodosgolpistas",
            "ForaTemer", "foraTemer", "foratemer", "Foratemer", "DiretasJá",
             "DiretasJa", "diretasjá", "diretasja"]

assuntos = ["cunha", "Cunha"]

assuntos = ["lula", "Lula", "LulaAcabou", "lulaacabou", "Lulaacabou", "lulaAcabou"]

"""
assuntos = ["João Doria", "joão doria", "joao doria" "Doria", "doria", "Celso Russomano", "Celso Russomano", "Russomano",
            "Russomano", "russomano", "russomanno", "celso russomano", "celso russomanno", "Fernando Haddad",
            "fernando haddad", "Haddad", "haddad", "Marta", "marta", "Luiza Erundina", "luiza erundina", "Erundina",
            "erundina", "Levy Fidélix", "levy fidélix", "levy fidelix", "Levy Fidelix", "Aidan", "aidan", "Paulo Serra",
            "paulo serra", "Ailton Lima", "ailton lima", "Rafael Daniel", "rafael daniel", "Ricardo Alvares",
            "ricardo alvares", "Carlos Grana", "carlos grana", "Alex Manente", "alex manente", "Orlando Morando",
            "orlando morando", "Tarcisio Secoli", "tarcisio secoli", "Aldo Santos", "aldo santos", "Cesar Raya",
            "cesar raya", "Tunico Vieira", "tunico vieira", "Paulo Pinheiro", "paulo pinheiro", "Auricchio", "auricchio,"
            "Gilberto Costa", "gilberto costa", "Fabio Palacio", "fabio palacio", "Lucia dal Mas", "lucia dal mas",
            "Marcio Della Bella", "marcio della bella", "Ambientalista Virgílio", "ambientalista virgilio", "Lauro Michels",
            "lauro michels", "Ivanci", "ivanci", "Marcio Chaves", "marcio chaves", "Atila Jacomussi", "atila jacomussi",
            "Clovis Volpi", "clovis volpi", "Professora Rejane", "professora rejane", "Donisete Braga", "donisete braga",
            "Gilberto Barros", "gilberto barros", "Carlos Sacomani", "carlos sacomani", "Dedé da Folha", "dedé da folha",
            "Rosana Figueiredo", "rosana figueiredo", "Grecco", "grecco", "Kiko", "kiko", "Claudinho da Geladeira",
            "claudinho da geladeira", "Gabriel Maranhão", "gabriel maranhão", "Edvaldo Guerra", "edvaldo guerra",
            "Clesson Alves", "clesson alves"]

stream.statuses.filter(track = assuntos)
