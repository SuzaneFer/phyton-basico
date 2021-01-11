import matplotlib.pyplot as plt

#Gráfico de Linha
x = [1, 2, 3, 4, 5]
y = [2, 3, 7, 1, 0]

titulo = "Gráfico de barras"
eixox = "Eixo X"
eixoy = "Eixo Y"

# Legendas
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

#plt.plot(x,y)

#Gráfico de Barras
x = [1, 2, 3, 4, 5]
y = [2, 3, 7, 1, 0]

titulo = "Gráfico de barras"
eixox = "Eixo X"
eixoy = "Eixo Y"

# Legendas
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

#plt.bar(x,y)



# Comparando gráficos de barras
x1 = [1, 3, 5, 7, 9]
y1 = [2, 3, 7, 1, 0]

x2 = [2, 4, 6, 8, 10]
y2 = [5, 1, 3, 7, 4]

titulo = "Gráfico de barras 2"
eixox = "Eixo X"
eixoy = "Eixo Y"

# Legendas
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

#plt.bar(x1, y1, label = "Grupo 1")
#plt.bar(x2, y2, label = "Grupo 2")
#plt.legend()


# Gráfico de dispersão
x = [1, 3, 5, 7, 9]
y = [2, 3, 7, 1, 0]


titulo = "Gráfico de dispersão"
eixox = "Eixo X"
eixoy = "Eixo Y"

# Legendas
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

plt.scatter(x, y, label="Meus pontos", color="g", marker=".", s=100)
plt.plot(x,y, color = "k", linestyle = "--" )
plt.legend()

plt.show()

