#Neste estudo de caso, faremos a comparação entre duas sequências de DNA: 
# (1) ser humano; vs. (2) bactéria.

import matplotlib.pyplot as plt
import random

entrada = open("bacteria.fasta").read()
saida = open("bacteria.html","w")

cont = {}

# Dicionário
for i in ['A', 'T', 'C', 'G']:
    for j in ['A', 'T', 'C', 'G']:
        cont[i+j]=0

# Para tirar a quebra de linha
entrada = entrada.replace("\n"," ")

for k in range(len(entrada)-1):
    cont[entrada[k]+entrada[k+1]] += 1

# Printar em HTML

i = 1
for k in cont:
    transparencia = cont[k]/max(cont.values()) #pegar o maior valor
    saida.write("<div style='width:100px; border:1px solid #111; height: 100px; float: left; background-color:rgba(0,0,255, "+str(transparencia)+"')></div>")

saida.close()