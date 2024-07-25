# Número par o impar:
# Escribe un programa que pida al usuario un número e indique si es par o impar.

def par_impar(num):
    if num % 2 == 0: # Si el residuo de dividir num entre 2 es 0, el programa devuelve 'Par', sino ejecuta la siguiente sentencia.
        print('Es par')
    else:
        print('Es impar')

num = int(input('Numero: '))

par_impar(num)