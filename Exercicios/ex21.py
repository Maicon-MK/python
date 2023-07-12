#Crie um jogo que faça o computador pensar em um numero de 0 a 5 
#permite ter um chute para acerta

from random import randint 
CPU = (randint(0,5))
chute = int(input("Chute um numero de 0 a 5:"))


if chute == CPU:
    print(f"Seu numero: {chute}\n Computador: {CPU} \n Parabens, voce consegiu!")


else:
    print(f"Seu numero: {chute}\n Computador: {CPU} \n ERROUW!")

