# Comparación de números: Escribe un programa que solicite dos 
# números al usuario y luego imprima "True" si ambos números son iguales
# y "False" si son diferentes.

def numeros(num1,num2):
    if num1 == num2:
        return True
    else: 
        return False

num1 = int(input('Numero 1: '))
num2 = int(input('Numero 2: '))

print(numeros(num1,num2))
