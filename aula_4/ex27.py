# Diga  se é possivel formar um triangulo com os lados indicados.

l1 = int(input('Digite um valor para ser o primeiro lado: '))
l2 = int(input('Digite um valor para ser o segundo lado: '))
l3 = int(input('Digite um valor para ser o terceiro lado: '))

if (((abs(l2 - l3)) < l1 < (l2 + l3)) and ((abs(l1 - l3)) < l2 < (l1 + l3))
        and ((abs(l1 - l2)) < l3 < (l1 + l2))):
    print("É possível formar um triângulo!")
else:
    print("Não é possível formar um triângulo!")