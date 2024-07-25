# Juego de ahorcado: 
# Desarrolla el clásico juego de "ahorcado" donde un jugador tiene que adivinar una palabra secreta. 
# Crea funciones para manejar las rondas de juego, 
# la visualización de progreso y la verificación de letras ingresadas por el jugador.

import random

def obtener_palabra():
    palabaras = ['python','javascript','java','c','r','ruby','assembly','swift','go','php'] #Creamos una Lista con valores establecidos
    palabra_aleatoria=random.choice(palabaras) #El metodo random.choice() selecciona un elemento aleatorio de la lista creada
    return palabra_aleatoria

def mostrar_tablero(palabra_secreta,letras):
    tablero = ''
    for letra in palabra_secreta:
        if letra in letras:
            tablero += letra
        else:
            tablero += '*'
    print(tablero)

def jugar():
    palabra_secreta = obtener_palabra()
    letra_adivinada = []
    intentos = 3

    while intentos > 0 :
        mostrar_tablero(palabra_secreta, letra_adivinada)
        letra = input('Intoduce una letra: ').lower()
        if letra in letra_adivinada:
            print('Letra ya introducida: ')
            continue
        elif letra in palabra_secreta:
            letra_adivinada.append(letra)
            if set(letra_adivinada) == set(palabra_secreta):
                print('Felicitaciones!! Has Ganado')
                break
        else:
            intentos -= 1
            print('Letra incorrecta te quedan: ',intentos,'intentos...')

    if intentos == 0:
        print('Has perdido, la palabra es: ',palabra_secreta)
print('ADIVINA EL LENGUAJE DE PROGRAMACION')

if __name__=='__main__':
    jugar()