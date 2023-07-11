# Faça um programa que leia o nome de 4alunos e escreva na tela
# e escreva na tela o nome do escolhido para apagar o quadro
from random import choice

Aluno1 = input("Digite o nome do 1° aluno: ")
Aluno2 = input("Digite o nome do 2° aluno: ")
Aluno3 = input("Digite o nome do 3° aluno: ")
Aluno4 = input("Digite o nome do 4° aluno: ")
alunos = Aluno1, Aluno2, Aluno3, Aluno4

print(choice(alunos))
