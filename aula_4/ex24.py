# faça um programa que leia a distancia em km de uma viagem, se a distancia dor menor ou igual a 200km cobre 50 centavos por km rodado, caso contrario cobre 45 centavos.

km = float(input('Quantos kilometros foram percorridos? '))

if km <= 200.0:
    print(f'O valor da corrida é de: {km*0.5} reais')

elif km >= 201.0:
    print(f'O valor da corrida é de: {km*0.45} reais')