# Tabla de multiplicar: 
# Crea un programa que pida al usuario un número y 
# muestre la tabla de multiplicar de ese número del 1 al 10 utilizando un bucle for.

num = int(input('Numero: '))
for x in range(1,11):
    resultado = num * x
    print(num,'x',x,'=', resultado)