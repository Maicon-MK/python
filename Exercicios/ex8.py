numero = int(input("Escreva seu numero:"))
# IMPAR = Multiplica a variavel impar por  resto da divisao se for igual a 1 impar 
# PAR = Mutiplica o resultado da vairavel par por resto da divisao -1 se for igual a 0 e par 
paridade = "impar" * (numero%2  ) + "par" * (1 - numero % 2)
print(f"O numero{paridade}")