# Lista de números pares: 
# Escribe un programa que tome una lista de números y devuelva una nueva lista solo con los números pares.

numeros = [1,2,3,5,6,8,10]
for x in numeros:
    if x % 2 == 0:
        print('Numeros Pares: ', x)