# Diccionario de estudiantes: 
# Crea un diccionario que contenga información básica de varios estudiantes (nombre, edad, grado)
# y luego escribe funciones para agregar un nuevo estudiante, 
# eliminar un estudiante existente y mostrar todos los estudiantes

diccionario = {}

def agregar():
    datos = int(input('Ingrese la cantidad de estudiantes a registrar: '))
    for x in range(datos):
            nombre = input('Ingrese nombre del Estudiante: ')
            edad = int(input('Ingrese edad: '))
            grado = input('Ingrese grado: ')
            datos=[nombre,edad,grado]
            diccionario[nombre] = datos
    
def mostrar(dicc_students):
    for id, students in enumerate(dicc_students.values(), start = 1):
        print('ID: |',id,'| |Estudiante: ',students[0],'| |Edad: ',students[1],'| |Grado: ',students[2],'|')
    
def eliminar():
    mostrar(diccionario)
    id= int(input('Ingrese un ID a eliminar: '))
    if 1 <= id <= len(diccionario): 
        del diccionario[list(diccionario.keys())[id - 1]]
        print('Estudiante eliminado correctamente')
    else:
        print('ID no valido')

def menu():
    while True:
        print('(1) AGREGAR ESTUDIANTES ')
        print('(2) MOSTRAR ESTUDIANTES ')
        print('(3) ELIMINAR ESTUDIANTES ')
        print('(X) SALIR ')
        op = input('Ingrese una opcion: ').upper()
        if op == 'X':
            print('Saliendo...')
            break
        elif op =='1':
            agregar()
        elif op == '2':
            mostrar(diccionario)
        elif op =='3':
            eliminar()
        else:
            print('Ingrese una opcion valida')
            return
if __name__=="__main__":
    menu()