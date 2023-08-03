# leia um triangulo qualquer e mostre na tela o valor
# do seno, cosseno e tangente desse angulo

from math import sin, cos, tan, radians

angulo = float(input("De valor ao angulo: "))

print(sin(radians(angulo)))
print(cos(radians(angulo)))
print(tan(radians(angulo)))