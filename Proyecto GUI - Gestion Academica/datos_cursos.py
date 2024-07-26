import tkinter as tk
from tkinter import *
from tkinter import messagebox, ttk
from connect_bd import *
import datos_profesor
import datos_estudiantes

def interfaz_cursos():

    root = tk.Tk()
    root.title('Gestion Academica')
    root.geometry('550x450')
    root.config(background='#FFFFFF')
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    root.resizable(False, False)
    root.iconbitmap('Ruta del ico') #Ruta del icono
    
    def salir():
        root.destroy()
        
    def button_reset():
        entry_id_curso.delete(0,END)
        campo_anio_curso.set('Elige una Opcion')
        campo_division.set('Elige una Opcion')
        campo_orientacion.set('Elige una Opcion')
        
    def menu_estudiantes():
        root.destroy()
        datos_estudiantes.interfaz_estudiantes()

    def menu_profesor():
        root.destroy()
        datos_profesor.interfaz_profesor()
        
    def es_entero_year(num):
        try:
            entero = int(num)
            if 0 <= entero <= 10:
                return True
            else:
                return False
        except ValueError as error:
            print('El numero ingresado no es entero'.format(error))
    
    def es_entero_division(num):
        try:
            entero = int(num)
            if 0 <= entero <= 3:
                return True
            else:
                return False
        except ValueError as error:
            print('El numero ingresado no es entero'.format(error))

    def validar_orientacion():
        if select_curso.get() not in ['Orientacion 1','Orientacion 2','Orientacion 3']:
            return False
        return True
    
    def guardar_registros():
        try:
            year = campo_anio_curso.get()
            division = campo_division.get()   
            orientacion = campo_orientacion.get()
            
            if not year or not division or not orientacion or year == 'Elige una Opcion' or division == 'Elige una Opcion' or orientacion == 'Elige una Opcion': 
                messagebox.showerror('¡Error!','Completa todos los campos')
                return

            if not es_entero_year(year):
                messagebox.showerror('¡Error!','Ingrese un año valido')
                return
            
            if not es_entero_division(division):
                messagebox.showerror('!Error!','Ingrese una division valida')
                return
            
            if not validar_orientacion():
                messagebox.showerror('¡Error!','Seleccione una Orientacion valida') 
                return 

            conexion_curso.carga_datos_curso(year,division,orientacion)
            messagebox.showinfo('Info','Los datos fueron guardados')

            actualizar_tabla()

            campo_anio_curso.set('Elige una Opcion')
            campo_division.set('Elige una Opcion')
            campo_orientacion.set('Elige una Opcion')
        
        except ValueError as error:
            print('Error al ingresar datos'.format(error))

    def actualizar_tabla():
        try:
            tabla_datos.delete(*tabla_datos.get_children())
            datos = conexion_curso.mostrar_curso()
            for row in datos:
                tabla_datos.insert('','end',values=row)

        except ValueError as error:
            print('Error al actualizar tabla'.format(error))
    
    def seleccionar_registros(evento):
        try:
            select= tabla_datos.focus()
            if select:
                values = tabla_datos.item(select)['values']
                entry_id_curso.delete(0,END)
                entry_id_curso.insert(0,values[0])
                campo_anio_curso.set(values[1])
                campo_division.set(values[2])
                campo_orientacion.set(values[3])
        except ValueError as error:
            print('Error al seleccionar registros'.format(error))

    def modificar_registro():
        try:
            id_curso = entry_id_curso.get()
            year = campo_anio_curso.get()
            division = campo_division.get()
            orientacion =campo_orientacion.get()

            if not id_curso or not year or not division or not orientacion or year == 'Elige una Opcion' or division == 'Elige una Opcion' or orientacion == 'Elige una Opcion':
                messagebox.showerror('¡Error!','Los valores no estan inicializados')
                return
            
            if not es_entero_year(year):
                messagebox.showerror('¡Error!','Ingrese un año valido')
                return
            
            if not es_entero_division(division):
                messagebox.showerror('¡Error!','Ingrese una divsion valida')
                return
            
            if not validar_orientacion():
                messagebox.showerror('¡Error!','Ingrese una orientacion valida')
                return

            conexion_curso.modificar_curso(id_curso,year,division,orientacion)
            messagebox.showinfo('Info','Los datos fueron modificados')
            
            actualizar_tabla()

        except ValueError as error:
            print('Error al modificar los datos'.format(error))
    
    def eliminar_registros():     
        try:
            id_curso = entry_id_curso.get()

            if not id_curso:
                messagebox.showerror('¡Error!','Los valores no estan inicializados')
                return
            
            conexion_curso.eliminar_curso(id_curso)
            messagebox.showinfo('Info','Los datos fueron eliminados correctamente')
            actualizar_tabla()

            entry_id_curso.delete(0,END)
            campo_anio_curso.set('Elige una Opcion')
            campo_division.set('Elige una Opcion')
            campo_orientacion.set('Elige una Opcion')
      
        except ValueError as error:
            print('Error al eliminar datos'.format(error))

    def eliminar_profesor():
        try:
            select = tabla_datos.focus()
            
            if not select:
                messagebox.showerror('¡Error!','No hay datos seleccionados')
                return
            
            values = tabla_datos.item(select)['values']
            if not values:
                messagebox.showerror('¡Error!','No hay datos seleccionados')
                return
            
            id_curso = values[0]
            id_profesor = values[4]
            if id_profesor is None or id_profesor =='None':
                messagebox.showerror('¡Error!','Profesor inexistente')    
                return
                   
            profesor_curso.eliminar_profesor(id_profesor,id_curso)
            messagebox.showinfo('Info','Profesor eliminado Correctamente')

            actualizar_tabla()

        except ValueError as error:
            print('Error al eliminar Profesor del curso'.format(error))

# FRAME Datos del curso 

    label_curso = LabelFrame(root)
    label_curso.grid(row=0,column=0,padx=5,pady=5)
    label_curso.config(background='#FFFFFF', borderwidth=0)

    datos_curso = Label(label_curso, text='Datos del Curso ')
    datos_curso.grid(row=0,column=0, padx=5,pady=5,columnspan=3)
    datos_curso.config(font=('Poppins', 20, 'bold'), fg='#1E3A5F', bg='#FFFFFF')
    

    id_curso = Label(label_curso,text='ID Curso')
    id_curso.grid(row=1,column=0, padx=5, pady=5, sticky='e')
    id_curso.config(font=('Poppins', 12, 'bold'), fg='#000000', bg='#FFFFFF')

    entry_id_curso = Entry(label_curso)
    entry_id_curso.grid(row=1, column=1, padx=5, pady=5, sticky='w')
    entry_id_curso.config(font=('Poppins', 12), fg='#000000', bg='#FFFFFF')

# Style para Combobox  
    style = ttk.Style()
    style.theme_use('default')
    style.configure('TCombobox', fieldbackground='#FFFFFF', background='#77DD77', foreground='#000000', font=('Poppins', 12))
    style.map('TCombobox', fieldbackground=[('readonly', '#FFFFFF')])

    year = [int(i) for i in range(1,7)]
    curso_anio = Label(label_curso,text='Año')
    curso_anio.grid(row=2,column=0, padx=5, pady=5,sticky='e')
    curso_anio.config(font=('Poppins', 12, 'bold'), fg='#000000', bg='#FFFFFF')
    campo_anio_curso = ttk.Combobox(label_curso,values=year, style='TCombobox')
    campo_anio_curso.grid(row=2,column=1, padx=5, pady=5, sticky='w')
    campo_anio_curso.set('Elige una Opcion')

    division = [int(i) for i in range(1,4)]
    curso_division = Label(label_curso,text='Division')
    curso_division.grid(row=3,column=0, padx=5, pady=5, sticky='e')
    curso_division.config(font=('Poppins', 12, 'bold'), fg='#000000', bg='#FFFFFF')
    campo_division = ttk.Combobox(label_curso,values=division, style='TCombobox')
    campo_division.grid(row=3,column=1, padx=5, pady=5,sticky='w')
    campo_division.set('Elige una Opcion')

    curso_orientacion = Label(label_curso,text='Orientacion') 
    curso_orientacion.grid(row=4,column=0, padx=5, pady=5, sticky='e')
    curso_orientacion.config(font=('Poppins', 12, 'bold'), fg='#000000', bg='#FFFFFF')
    select_curso = StringVar()
    campo_orientacion = ttk.Combobox(label_curso,values=['Orientacion 1','Orientacion 2','Orientacion 3'],textvariable=select_curso, style='TCombobox')
    campo_orientacion.grid(row=4,column=1, padx=5, pady=5, sticky='w')
    select_curso.set('Elige una Opcion')

# ------------------------ BOTONES ---------------------------

    button_guardar = Button(label_curso,text='Guardar',command=guardar_registros, width=10, height=1)
    button_guardar.grid(row=1,column=2, columnspan=2)
    button_guardar.config(font=('Poppins', 10), bg='#90EE90',fg='#000000')

    button_modificar = Button(label_curso, text='Modificar',command=modificar_registro,width=10, height=1)
    button_modificar.grid(row=2,column=2,columnspan=2)
    button_modificar.config(font=('Poppins',10), bg='#90EE90', fg='#000000')

    button_eliminar = Button(label_curso, text='Eliminar',command=eliminar_registros, width=10, height=1)
    button_eliminar.grid(row=3,column=2,columnspan=2)
    button_eliminar.config(font=('Poppins', 10), bg='#FF6F61', fg='#000000')
   
    reset = Button(label_curso, text='Reset',command=button_reset, width=10, height=1)
    reset.grid(row=4,column=2,columnspan=2)
    reset.config(font=('Poppins',10), bg='#FFD700', fg='#000000')
    
    quitar_profesor = Button(label_curso, text='Quitar Profesor', command=eliminar_profesor, width=15, height=1)
    quitar_profesor.grid(row=5, column= 2)
    quitar_profesor.config(font=('Poppins', 10), bg='#FF6F61', fg='#000000')

    button_add_estudiante = Button(label_curso,text='Ver o Agregar Estudiante',command=menu_estudiantes, width=20, height=1) 
    button_add_estudiante.grid(row=5,column=0)
    button_add_estudiante.config(font=('Poppins', 10), bg='#77DD77', fg='#000000')

    button_add_profresor = Button(label_curso,text='Ver o Asignar Profesor', command=menu_profesor, width=20, height=1) 
    button_add_profresor.grid(row=5,column=1, padx=10, pady=10)
    button_add_profresor.config(font=('Poppins', 10), bg='#77DD77', fg='#000000')

    # ---------------------- Treeview ---------------

    label_titulo  = LabelFrame(root)
    titulo = Label(label_titulo, text='Listado de Cursos',font=('Poppins', 19, 'bold'), fg='#1E3A5F', bg='#FFFFFF', pady=5, padx=5)
    titulo.pack()
    label_titulo.grid(row=7,column=0,padx=5, pady=5)
    label_titulo.config(background='#FFFFFF', borderwidth=0)
    tabla_datos = ttk.Treeview(label_titulo,columns=('ID','Anio','Division','Orientacion','Profesor'),show='headings',height=5)
    tabla_datos.column('# 1',anchor=CENTER)
    tabla_datos.heading('# 1',text='ID')
    tabla_datos.column('# 2',anchor=CENTER,width=100)
    tabla_datos.heading('# 2',text='Año')
    tabla_datos.column('# 3',anchor=CENTER,width=100)
    tabla_datos.heading('# 3',text='Division')
    tabla_datos.column('# 4',anchor=CENTER, width=150)
    tabla_datos.heading('# 4',text='Orientacion')
    tabla_datos.column('# 5',anchor=CENTER, width=150)
    tabla_datos.heading('# 5',text='Profesor')
    tabla_datos['displaycolumns'] = (1,2,3,4)

    scroll_vertical = Scrollbar(label_titulo, orient='vertical', command=tabla_datos.yview)
    tabla_datos.configure(yscroll=scroll_vertical.set)
    tabla_datos.pack(side='left', fill='both', expand=True)
    scroll_vertical.pack(side='right', fill='y')

    for row in conexion_curso.mostrar_curso():
        tabla_datos.insert('','end',values=row)

    tabla_datos.bind("<<TreeviewSelect>>",seleccionar_registros)

    button_salir = Button(root, text='Salir',command=salir, width=10, height=1)
    button_salir.grid(row=8, column=0, columnspan=2, padx=(10,5), pady=5)
    button_salir.config(bg='#FF6F61', font=('Poppins', 10), fg= '#000000')

    root.eval('tk::PlaceWindow . center')
    root.mainloop()

# interfaz_cursos() 
