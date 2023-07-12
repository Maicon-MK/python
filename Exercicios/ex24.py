#Faça um programa que leia a distancia em Km de uma viagem, se a distancia fot menor ou igual
#a 200Km cobre 50 centavos por km rodado, caso contrario cobre 45 centavos.

viagem = float(input("Qual a distancia da sua viagem?" ))

if viagem <= 200:
    print(f"O valor da sua viagem {viagem * 0.5} reais.")
elif viagem > 200:
    print(f" O valor da sua viagem e de {viagem * 0.45} reais")


                   