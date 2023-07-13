#Escreva um programa para aprovar o emprestimo bancario para a compra de uma casa.
#pergunte o valor da casa, o salario, quantos anos ele vai pagar.
#A aprestação mensal nao pode exceder 30% do salario ou o emprestimo será negado.

valor_casa = float(input("Qual eo valor da casa? "))

salario = float(input("Quanto você ganha de salario? "))

anos = int(input("Em quantas vezes? "))

meses = (anos/12)

prestacao = (valor_casa * meses)

if prestacao > 0.3 * salario:
    print( "acho que foi")
else:
    print("Foi nao mane!")