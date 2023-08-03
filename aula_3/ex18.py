# faça um programa que leia o nome de 4 alunos e escreva na tela
# o nome do escolhido para apagar o quadro

import random

from random import choice

n1 = (input("Diga o nome do primeiro aluno: "))
n2 = (input("Diga o nome do segundo aluno: "))
n3 = (input("Diga o nome do terceiro aluno: "))
n4 = (input("Diga o nome do quarto aluno: "))

print("Sorteio: {}". format(choice([n1, n2, n3, n4])))