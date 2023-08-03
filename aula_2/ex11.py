# faça um programa que leia o preço de um produto e retorne o seu preço com 5% de desconto

print("Informaremos o valor do produto com 5% de desconto")

p = float(input('Digite o valor do produto: '))
dp = (p * 0.05)

print(f'O desconto é de {dp} e seu preço descontado é de {p-dp}')