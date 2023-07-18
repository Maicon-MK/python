#Crie um programa que leia o numero de um usuario e mostre sua 
#tabuada de 1 a ate 10

numero = int(input("Digite um numero: "))
for resultado in range(numero,numero*11, numero ):
    print(f"resultado {resultado}")
   