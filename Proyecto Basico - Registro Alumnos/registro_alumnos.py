import os
def validar_enteros(num):
    try:
        if num > 0:
            return True
    except:
        return False
def validar_cadena(txt):
    if txt.isalpha():
        return True
    else:
        return False
    
def crearalu():
    print("----CREAR ALUMNO----")
    nom=input("Ingrese el nombre: ").capitalize()
    validar_nom = validar_cadena(nom)
    if not validar_nom:
        print('Ingresa un nombre valido')
        return
    
    ape=input("Ingrese el apellido: ").capitalize()
    validar_apellido = validar_cadena(ape)
    if not validar_apellido:
        print('Ingresa un apellido valido')
        return
    
    edad=input("Ingrese su edad: ")
    es_edad_valida = validar_enteros(edad) 
    if es_edad_valida:
       print('Ingresa una edad valida')
       return
    
    sexo=input("Ingrese M/(Masculino) F/(Femenino): ").upper()
    dni=input("Ingrese su DNI: ")
    validar_dni = validar_enteros(dni)
    if validar_dni:
        print('Ingrese un DNI valido')
        return
    
    curso=input("Ingrese el curso: ")
    validar_curso = validar_enteros(curso)
    if validar_curso:
        print('Ingrese un curso valido')
        return
    
    div=input("Ingrese la division: ")
    validar_division = validar_enteros(div)
    if validar_division:
        print('Ingrese una divsion valida')
        return
    
    notas=[]
    persona=[nom,ape,edad,sexo,dni,curso,div,notas]
    return persona

def listado(lista):
    for x in range(len(lista)):
        print(str(x)+"| "+lista[x][0]+" | "+lista[x][1]+" | "+lista[x][2]+" | "+lista[x][3]+" | "+lista[x][4]+" | "+lista[x][5]+" | "+lista[x][6]+" | "+str(lista[x][7]))

def editaralu(num):
    op=""
    while op!="7":
        print("---ALUMNO A EDITAR---")
        print(str(num)+" | "+alumnos[num][0]+" | "+alumnos[num][1]+" | "+alumnos[num][2]+" | "+alumnos[num][3]+" | "+alumnos[num][4]+" | "+alumnos[num][5]+" | "+alumnos[num][6])
        print("0- Nombre ")
        print("1- Apellido ")
        print("2- Edad ")
        print("3- Sexo ")
        print("4- DNI ")
        print("5- Curso ")
        print("6- Division ")
        print("7- Terminar edicion: ")
        op=input("Ingrese una opcion a editar: ")
        if op=="0":
            nombre=input("Ingrese el nuevo nombre: ").capitalize()
            validar_dato = validar_cadena(nombre)
            if not validar_dato:
                print('Ingrese un nombre valido')
                return
            else:
                alumnos[num][0]=nombre
        elif op=="1":
            apellido=input('Ingrese el apellido nuevo: ').capitalize()
            validar_apellido = validar_cadena(apellido)
            if not validar_apellido:
                print('Ingrese un apellido valido')
                return
            else:
                alumnos[num][1]=apellido
        elif op=="2":
            edad = input('Ingrese una nueva edad_ ')
            validar_edad = validar_enteros(edad)
            if validar_edad:
                print('Ingrese una edad valida')
                return
            alumnos[num][2]=edad
        elif op=="3":
            sexo=input("Ingrese M/(Masculino) F/(Femenino): ").upper()
            alumnos[num][3]=sexo
        elif op=="4":
            dni = input('Ingrese DNI nuevo: ')
            validar_dni = validar_enteros(dni)
            if validar_dni:
                print('Ingrese DNI valido')
                return
            alumnos[num][4]=dni
        elif op=="5":
            curso = input('Ingrese curso nuevo: ')
            validar_curso = validar_enteros(curso)
            if validar_curso:
                print('Ingrese un curso valido')
                return
            alumnos[num][5]=curso
        elif op=="6":
            division = input('Ingrese division nueva: ')
            validar_division = validar_enteros(division)
            if validar_division:
                print('Ingresa una division valida')
                return
            alumnos[num][6]=division
        else:
            print('Ingrese una opcion valida')

def crearnota(num):
    print("------"+alumnos[num][0]+"  "+alumnos[num][1]+"-------")
    nota=0
    while nota!="S":
        nota=input("Ingrese una nota o ''S'' para salir: ").upper()
        if nota=="S":
            print("Volviendo al menu principal...")
        else:
            alumnos[num][7].append(nota)
    
def editarnota(num):
	op=0
	while op!="X":
		print("--------"+alumnos[num][0]+" "+alumnos[num][1]+"--------")
		print("ID | NOTA")
		for x in range(len(alumnos[num][7])):
			print(str(x)+"  | "+alumnos[num][7][x])
		op=input("Ingrese el ID de la nota a editar o ''X'' para salir: ").upper()
		if op=="X":
			print("Volviendo al menu principal...")
		else:
			alumnos[num][7][int(op)]=input("Ingrese una nueva nota: ")
		os.system('cls')

alumnos=[]
op=""
while op!="6":
    print("----MENU----")
    print("1- Ingresar un alumno: ")
    print("2- Editar Alumno: ")
    print("3- Ingesar Nota: ")
    print("4- Editar Nota: ")
    print("5- Listado de Alumno")
    print("6- Exit ")
    op=input("Que desea hacer: ")

    if op=="1":
        alu=crearalu()
        alumnos.append(alu)
        os.system('cls')

    elif op=="2":
        print("----LISTADO DE ALUMNOS----")
        listado(alumnos)
        edi=int(input("Ingrese el ID del alumno a editar: "))
        editaralu(edi)
        os.system('cls')

    elif op=="3":
        print("----LISTADO DE ALUMNOS----")
        listado(alumnos)
        edi=int(input("Ingrese el ID del alumno para agregar nota: "))
        crearnota(edi)
        os.system('cls')

    elif op=="4":
        print("----LISTADO DE ALUMNOS----")
        listado(alumnos)
        edi=int(input("Ingrese el ID del alumno para editar las notas: "))
        editarnota(edi)
    
    elif op=="5":
        print("ID|")
        listado(alumnos)
        input("Presione ENTER para continuar....")
        os.system('cls')
    else:
        print('Ingrese una opcion correcta')
        os.system('cls')