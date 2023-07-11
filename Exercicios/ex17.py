# ex017 Leia um ângulo qualquer e mostre na tela o valor de seno,consseno e tangente desse angulo

from math import sin, cos, tan, radians

Angulo = float(input("Lado A: "))
print(
    f" {sin(radians(Angulo))} Seno\n, {cos(radians(Angulo))} Consenno \n {tan(radians(Angulo))} Angulo"
)
