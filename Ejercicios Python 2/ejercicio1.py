# Conteo de Palabras:
# Escribe un programa que reciba una cadena de texto como entrada y 
# cuente la frecuencia de cada palabra en el texto utilizando un diccionario. P
# or ejemplo, dado el texto "hola mundo hola", el programa debería producir un diccionario que
# mapee cada palabra a su frecuencia de aparición, como {'hola': 2, 'mundo': 1}.

palabras = {}

def contar_palabras(texto):
    palabra = texto.split()
    for x in palabra:
        palabras[x]=palabras.get(x,0)+1
    return palabras

texto = input('Ingrese un texto: ')
contar_palabras(texto)
print('Frecuencia Palabras: ',palabras)