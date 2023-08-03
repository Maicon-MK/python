# Elabora um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - À vista dinheiro/cheque: 10% de desconto
# - À vista no cartão: 5% de desconto
# - Em até 2x no cartão: preço formal
# - 3x ou mais no cartão: 20% de juros

valor = float(input('Digite o valor do produto: '))
forma = int(input('Diga a forma de pagamento.\n A vista dinheiro ou cheque [1]\n A vista no cartão [2]\n Em até 2x no cartão [3]\n 3x ou mais no cartão [4]\n Escolha: '))

desconto10 = valor * 0.1
desconto5 = valor * 0.05
cartao3x = valor * 0.2

if forma == 1:
    print(f'Total do produto: {valor - desconto10} reais')

elif forma == 2:
    print(f'Total do produto: {valor - desconto5} reais')

elif forma == 3:
    print(f'Total do produto: {valor} reais')

elif forma == 4:
    print(f'Total do produto: {valor + cartao3x} reais')