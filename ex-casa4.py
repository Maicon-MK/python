#Fibonacci com Recursão: Escreva uma função que calcule o n-ésimo
# número da sequência de Fibonacci usando recursão.

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1 
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Digite um número: ")) 
resultado = fibonacci(n)
print(f"O {n}-ésimo número de Fibonacci é {resultado}")
    