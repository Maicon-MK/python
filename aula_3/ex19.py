# agora, sorteie uma ordem aleatoria de 4 alunos. 
#leia o nome dos alunos e mostre 
#a ordem aleatoria

import random
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('Ordem de apresentação:')
print(lista)