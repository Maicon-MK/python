#Melhore o jogo de advinhação onde o computador "pensa" um numero.
#mosntre quantos palpites o usuario usou.
import random

def jogo_advinhacao():
   
    numero_pensado = random.randint(1, 10)
    tentativas = 0
    palpite = list()
    while palpite != numero_pensado:
        
            palpite = int(input("Digite o seu palpite: ")).append
        

            if palpite == numero_pensado:
                print(f"Parabéns! Você acertou o número {numero_pensado} em {tentativas} tentativas!")
                
            elif palpite < numero_pensado:
                print("Tente um número maior.")
            else:
                print("Tente um número menor.")
        

jogo_advinhacao()





