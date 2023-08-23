# #Loop Dicionario 
# #dicionario ela guarda  um valor 
# estado = dict()
# #lista 
# pais = list()
# for loop
# for c in range (3):
#   estado ["UF"] = input("Qual eo nome do estado")
#   estado ["Sigla"] = input("Qual ea sigla do estado")
# pais.append(estado.copy())

# #O primeiro for entra lista para pegar a chave eo valor.
# for e in pais:
#   #V recebe os valores do lista no caso o estado e a sigla
#   for v in e.items():
#     print(v)

# Crie um programa que simule uma corrida entre dois carros,
# onde os carros avançam a cada interação do loop. O carro A eo o carro B
# começam na posição. cada carro avança uma distancia aleatoria entre 1 e 5.
# o carro que atingir a posição 30 primeiro e daclarado o vencedor.
from random import randint
import random

CA = 0
CB = 0

gas_A = random.randint(1,5)
gas_B = random.randint(1,5)

while CA <= 30 or CB <= 30:
    CA + gas_A
    CB += gas_B
    if CA == 30:
        print("CA FOI O VENCEDOR")
    elif CB == 30:
        print(" CB FOI VENCEDOR")
    if CA == 30 and CB == 30:
        print("EMPATE")




