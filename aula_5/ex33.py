# a confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JÚNIOR
# - Até 25 anos: SENIOR
# - Acima de 25 anos: MASTER

ano = int(input('Digite seu ano de nascimento: '))
categoria = 2023 - ano

if categoria < 9:
    print('Sua categoria é mirim.')

elif 15 > categoria > 9:
    print('Sua categoria é infantil.')

elif 20 > categoria > 14:
    print('Sua categoria é infantil.')

elif  26 > categoria > 19:
    print('Sua categoria é infantil.')

else:
    print('Sua categoria é master.')