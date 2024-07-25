# Calculadora de Calificaciones:
# Crea un programa que calcule el promedio de calificaciones de varios estudiantes 
# utilizando un diccionario donde las llaves sean los nombres de los estudiantes
# y los valores sean listas de sus calificaciones.

estudiantes = {
    'Pepe':[10,4,6,8],
    'Juan':[4,5,3,4],
    'Maritn':[7,8,9,10]
}

def calcular_promedio(lista):
    if len(lista) < 0:
        return 0
    else:
        suma = sum(lista)
        promedio = suma / len(lista)
        return suma, promedio

for estudiante, calificaciones in estudiantes.items():
    suma, promedio = calcular_promedio(calificaciones)
    print('Estudiante:',estudiante,':','Total =', suma,':','Promedio =', promedio) 
