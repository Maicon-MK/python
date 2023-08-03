# faça um programa que leia 3 valores e diga o maior e o menor valor

a = float(input('Digite um valor: '))
b = float(input('Digite um valor: '))
c = float(input('Digite um valor: '))

if a > b and a > c:
    print('a é o maior valor')

elif b > a and b > c:
    print('b é o maior valor')

elif c > a and c > b:
    print('c é o maior valor')

if a < b and a < c:
    print('a é o menor valor')

elif b < a and b < c:
    print('b é o menor valor')

elif c < a and c < b:
    print('c é o menor valor')