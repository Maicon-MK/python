#Crie uma função que chamada "Divide_numbers" que recebe
#Dois parametros numero a e b e retorna a divisao de a por b
#Ultilize try e except para tratar a divisão por zero.

def divide_numbers(a, b):
    try:
        result = a/b
        
    except ZeroDivisionError:
        print("Digite numero interios.")
        result 
    else:
        print(f"{a} divido por {b} e igual a {result}")

divide_numbers(int(input("Digite o 1 valor: ")), int(input("Digite o 2 valor: ")))

