"""Desenvolva um programa que calcule a soma de todos numeros
multiplos de 1 e 500
Bonus: E mostre quantos numero que sao divisiveis """

soma = 0
divisiveis = 0

for num in range(1, 501):
    if num % 3 == 0:
        soma += num
        divisiveis += 1

print(f"A soma e: {soma}")
print(f"A quantida de numeros divisiveis por três é {divisiveis}")
