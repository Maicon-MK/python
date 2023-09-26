#2. Crie uma função que receba dois números como parametro e retorne a soma deles. Por exemplo, se a função for chamada de adicionar,
# chamar adicionar(1,2) deve retornar 3.

def add(x, y):
    return x + y

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

resultado = add(numero1, numero2)
print(resultado)