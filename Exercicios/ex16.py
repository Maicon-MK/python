#ex16:Leia o comprimento de cateto oposto e do adjacente
#de um triangulo retangulo. Calcule e mostre o comprimento da impotenusa. 

from math import hypot

CO = float( input("De o valor do cateto oposto: "))
CA = float(input("De o valor do adjecente:  "))

print(hypot(CO,CA))



