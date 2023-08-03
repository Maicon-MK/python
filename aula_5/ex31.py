# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade, se ele ainda vai se alistar ao serviço militar,
# se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# seu programa também deverá mostrar o tempo que galta ou que passou do prazo.

nasc = int(input('Diga seu ano de nascimento: '))
ano = 2023
tempo = ((ano - nasc) - 18)

if ano - nasc < 18:
    print('Você ainda irá se alistar ao serviço militar.')
    print(f'faltam {abs(tempo)} anos para se alistar.')

elif ano - nasc == 18:
    print('Está na hora de se alistar ao serviço militar.')

elif ano - nasc > 18:
    print('Você já deveria ter se alistado no serviço militar.')
    print(f'Está atrasado', abs(tempo) ,'anos.')
