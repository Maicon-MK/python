# Refaça o desafio 35 dos triangulos, acrescentado o recurso de mostrar que tipo de triangulo sera formado:
# - EQUILATERO: Todos os lados iguais
# - ISÓSCELES: dois lados iguais, um diferente
# - ESCALENO: todos os lados diferentes

l1 = float(input('Digite o valor do lado 1: '))
l2 = float(input('Digite o valor do lado 2: '))
l3 = float(input('Digite o valor do lado 3: '))

existe = (l1 + l2 > l3) or (l1 + l3 > l2) or (l2 + l3 > l1)

if existe == True:
    print('o triângulo existe')
    
    if l1 == l2 == l3:
        print('Equilatero')

    elif l1 == l2 != l3 or l2 == l3 != l1 or l1 == l3 != l2:
        print('Isósceles')

    elif l1 != l2 != l3:
        print('Escaleno')

else:
    print('o triângulo não existe')


