# Traductor Simple:
# Implementa un traductor básico que utilice un diccionario para almacenar las traducciones de palabras. 
# El programa debe tomar una palabra en inglés como entrada y devolver su traducción en español.

traductor = {'blue':'azul',
             'yellow':'amarillo',
             'black':'negro'}

def traduccion(palabra):
    return traductor.get(palabra.lower(), 'traduccion no encontrada' )
        
print('Listado de Palabras:')
for x in traductor.keys():
    print(x) 

traducir_palabra = input('Ingrese una palabra a traducir: ')
palabra = traduccion(traducir_palabra)
print('La traduccion de:',traducir_palabra,'es',palabra)
