#Ordenação de Lista: Implemente um algoritmo de ordenação 
#(por exemplo, Bubble Sort ou Selection Sort) 
#para ordenar uma lista de números.

def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        trocou = False

        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocou = True

        if not trocou:
            break

lista = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(lista)

print("Lista ordenada:", lista)

