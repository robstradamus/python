# Suma de elementos en lista: 
# Escribe una función que tome una lista de números y
# devuelva la suma de todos los números mayores que un valor dado. 
# Usa estructuras de control y bucles para lograrlo.

def numeros(num_lista, valor_mayor):
    suma = 0
    for x in num_lista:
        if x > valor_mayor:
            suma += x
    return suma

num_lista = [2,3,4,5,6,7,8]
valor_mayor = 7
resultado = numeros(num_lista, valor_mayor)
print('Valor Limite:',valor_mayor,'Suma de todos los numeros:',resultado)