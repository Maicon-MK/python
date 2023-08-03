# leia o comprimento do cateto oposto e do cateto adjacente
# de um triângulo retangulo. Calcule o comprimento da hipotenusa

from math import hypot

CO = float(input("De valor ao cateto oposto: "))
CA = float(input("De valor ao cateto adjacente: "))

print(hypot(CO,CA))