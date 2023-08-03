# Desenvolva uma logica que leia o peso e a altura de uma pessoa, calcule seu indice de massa corporal (imc) e mostre seu status, de acordo com a tabela abaixa:
# - IMC abaixo de 18,5: Abaixo do Peso
# - Entre 18,5 e 25: Peso Ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade Mórbida

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura em metros: '))

imc = (peso / altura**2) 

print(imc)

if imc < 18.5:
    print('Abaixo do peso')

elif  25 > imc > 18.5:
    print('Peso Ideal')

elif  30 > imc > 25:
    print('Sobre peso')

elif  40 > imc > 30:
    print('Obesidade')

elif  imc > 40:
    print('Obesidade Mórbida')