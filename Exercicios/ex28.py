# Escreva um programa que leia  dois numeros inteiros e compare-os.
# Mosta na tela uma mensagem:

# -O primeiro valor e maior;
# -O segundo valor e maior;
# -Nao existe valor maior, os dois sao iguais;

valor1 = int(input("Digite um numero: "))
valor2 = int(input("Digite outro numero: "))


if valor1 > valor2:
    print(f"Esse numero e maior {valor1}\n Esse eo menor {valor2}")
elif valor1 == valor2:
    print("Os valores são iguais!")
    
else:
    print(f"Esse eo numero eo maior {valor2}\n Esse numero eo menor {valor1}")
