# Suma de números pares: 
# Escribe un programa que sume todos los números pares del 1 al 100 utilizando un bucle for.

suma = 0
for num in range(1,101): 
    if num % 2 == 0: # Si el numero es par se añade a la variable suma
        suma += num

print(suma)