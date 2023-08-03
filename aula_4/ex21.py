import random

n_pc = random.randint(0,5)

n_usuario = int(input('Digite um número de 0 a 5: '))

if n_usuario == n_pc:
    print('Você ganhou!')

else:
    print('Você perdeu!\n'f'O número correto era {n_pc}')
