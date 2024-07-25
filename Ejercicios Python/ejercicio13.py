# Ordenamiento de lista:
# Implementa un algoritmo de ordenamiento (como el método de burbuja o el de selección) 
# para ordenar una lista de números de menor a mayor.

def ordenamiento_burbuja(lista):
    num = len(lista)
    for x in range(num):
        for j in range(0, num - x - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

num_lista = [80, 20, 40, 70, 30, 50]
print('Lista original: ', num_lista)
ordenamiento = ordenamiento_burbuja(num_lista)
print('Lista ordenada con Burbuja: ', ordenamiento)