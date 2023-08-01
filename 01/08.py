#Escreva um programa que peça ao usuario para digitar um numero inteiro e
#Em seguida  imprima o dobro desse numero  ultilize tray e excpet para lidar 
#com a possibilidade de o usuario inserir um valor nao numerico.

while True:
    try :
        num =  int(input("Digite um numero: "))
        result = num*2
        print(result)
    except:
        print('Digite um numero inteiro: ')


