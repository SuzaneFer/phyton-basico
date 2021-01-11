# Gráfico do crescimento da população brasileira de 1980-2016
# Coletado no DataSus

import matplotlib.pyplot as plt

dados = open("populacao_brasileira.csv").readlines()

x = []
y = []

for i in range(len(dados)):
    if i != 0:
        linha = dados[i].split(";")
        x.append(int(linha[0]))
        y.append(int(linha[1]))

plt.bar(x,y, color = "g")
plt.plot(x,y, color="r")
plt.title("Crescimento da população brasileira de 1980-2016")
plt.xlabel("Ano")
plt.ylabel("População x100.000.000")
plt.show()
#salvar a imagem
#plt.savefig("populacao_brasileira.png", dpi=300)
#dpi é utilizado para aumentar a qualidade da imagem

