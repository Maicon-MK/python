#DEF == CRIAR FUNÇÃO
"""numero  = int(input("Digite um numero: "))
def dobra(x):
    print(f"O dorbado é {x*2}")"""

def dobra(x=1):
    return x*2

numer_dobrado = dobra(4)
print(f"O numero dobrado e {numer_dobrado}")