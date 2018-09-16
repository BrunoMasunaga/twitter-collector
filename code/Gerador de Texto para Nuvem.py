database = open("Database.txt", 'r', encoding="utf8")
output = open("TextNuvem.txt", 'w', encoding="utf8")

for linha in database.readlines():
    textolinha = linha.split()
    termo = textolinha[0]
    quantidade = int(textolinha[1])/2
    i = 1
    while (i<=quantidade):
        output.writelines(termo + " ")
        i=i+1

database.close
output.close
