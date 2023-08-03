# Faça um programa que leia um número e diga se é par ou ímpar

num = int(input("Escolha um número: "))

print("O número é par" * (num % 2 == 0), "O número é ímpar" * (num % 2 != 0))