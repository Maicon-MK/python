# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))

media = (n1+n2)/2

if media < 6:
    print('você reprovou!')

elif media == 6:
    print('você foi aprovado na média.')

elif media > 6:
    print('Você passou com notas boas!')