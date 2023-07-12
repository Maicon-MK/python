# Faça um programa que leia a quilometragem de um carro, caso esteja acima dos 80km/h multe o carro.

carro = int(input("Qual e a velocidade do seu carro?"))
limite_de_velocidade = 80

if carro > limite_de_velocidade:
    print("Que isso mane {carro}Km/h e velozes e furiosos aqui!? Voce foi multado!")
else:
    print("Parabens cidadao de bem! voce esta pode seguir viagem! ")
