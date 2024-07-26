import tkinter as tk
from tkinter import *
from tkinter import messagebox, simpledialog, ttk
from connect_bd import *
import datos_cursos
  
def interfaz_estudiantes():

    def button_reset():
            estudiante_entry.delete(0,END)
            campo_nom_estudiante.delete(0,END)
            campo_ape_estudiante.delete(0,END)
            combo_sexo.set('Elige una Opcion')
            combo_edad.set('Selecciona una Edad')
            entry_legajo.delete(0,END)

    def volver():
            root.destroy()
            datos_cursos.interfaz_cursos()
        
    def es_entero(num):
            try:
                entero = int(num)
                if 0 <= entero <= 50:          
                    return True
                else:
                    return False
            except ValueError as error:
                print('El numero ingresado no es entero'.format(error))

    def validar_combo_sexo():
        if select_sexo.get() not in ['Masculino','Femenino']:
            return False
        return True
 
    def guardar_registro():
            try:
                nombre = campo_nom_estudiante.get()
                apellido = campo_ape_estudiante.get()
                sexo = combo_sexo.get()
                edad = combo_edad.get()
                legajo = entry_legajo.get()
                if not nombre or not apellido or not sexo or not edad or not legajo:
                    messagebox.showerror('¡Error!',' Completa todos los campos')
                    return
                if not es_entero(edad):
                    messagebox.showerror('¡Error!','Ingrese una edad valida')
                    return
                if not validar_combo_sexo():
                    messagebox.showerror('¡Error!','Seleccione un sexo valido')
                    return
                try:
                    conexion_estudiantes.carga_datos(nombre,apellido,sexo,edad,legajo)
                    messagebox.showinfo('Info','Los datos fueron guardados')
                except ValueError as error:
                    messagebox.showerror('¡Error!', str(error))
                    return
                except Exception as error:
                    messagebox.showerror('¡Error!','No se pudo insertar legajo en la Base de Datos')
                    return
                
                actualizar_tabla()

                campo_nom_estudiante.delete(0,END)
                campo_ape_estudiante.delete(0,END)
                combo_sexo.set('Elige una Opcion')
                combo_edad.set('Selecciona una Edad')
                entry_legajo.delete(0,END)

            except ValueError as error:
                print('Error al cargar los datos'.format(error))

    def actualizar_tabla():
            try:
                tabla_estudiantes.delete(*tabla_estudiantes.get_children())
                datos = conexion_estudiantes.mostrar_estudiante()
                for row in datos:
                    tabla_estudiantes.insert('','end',values=row)
            except ValueError as error:
                print('Error al actualizar datos'.format(error))
            
    def seleccionar_registros(evento):
            try:
                select = tabla_estudiantes.focus()
                if select: 
                    values = tabla_estudiantes.item(select)['values']

                    estudiante_entry.delete(0,END)
                    estudiante_entry.insert(0,values[0])
                    campo_nom_estudiante.delete(0,END)
                    campo_nom_estudiante.insert(0,values[1])
                    campo_ape_estudiante.delete(0,END)
                    campo_ape_estudiante.insert(0,values[2])
                    combo_sexo.set(values[3])
                    combo_edad.set(values[4])
                    entry_legajo.delete(0,END)
                    entry_legajo.insert(0,values[5])
            except ValueError as error:
                print('Error al seleccionar registros'.format(error))
        
    def modificar_registros():
            try:
                idEstudiante = estudiante_entry.get()
                nombre = campo_nom_estudiante.get()
                apellido = campo_ape_estudiante.get()
                sexo = combo_sexo.get()
                edad = combo_edad.get()
                legajo = entry_legajo.get()

                if not idEstudiante or not nombre or not apellido or not sexo or not edad or not legajo:
                    messagebox.showerror('¡Error!','Los valores no estan inicializados')
                    return
                
                if not es_entero(edad):
                    messagebox.showerror('¡Error!','Ingrese una de edad valida')
                    return
                
                if not validar_combo_sexo():
                    messagebox.showerror('¡Error!','Ingrese una opcion valida')
                    return
                
                if not validar_legajo(legajo):
                    messagebox.showerror('¡Error!','Ingrese un legajo valido')
                    return
                
                conexion_estudiantes.modificar_estudiante(idEstudiante,nombre,apellido,sexo,edad,legajo)
                messagebox.showinfo('Info','Datos actualizados')

                actualizar_tabla()

                estudiante_entry.delete(0,END)
                campo_nom_estudiante.delete(0,END)
                campo_ape_estudiante.delete(0,END)
                entry_legajo.delete(0,END)
            except ValueError as error:
                print('Error al modificar los datos'.format(error))
        
    def eliminar_estudiante():
            try:
                idEstudiante = estudiante_entry.get()

                if not idEstudiante:
                    messagebox.showerror('¡Error!','No hay datos seleccionados')
                    return
    
                conexion_estudiantes.eliminar_estudiante(idEstudiante)
                messagebox.showinfo('Info','Los datos fueron eliminados correctamente')
                
                actualizar_tabla()
                
                estudiante_entry.delete(0,END)
                campo_nom_estudiante.delete(0,END)
                campo_ape_estudiante.delete(0,END)
                combo_sexo.set('Elige una Opcion')
                combo_edad.set('Selecciona una Edad')
                entry_legajo.delete(0,END)
            
            except ValueError as error:
                print('Error al eliminar los datos'.format(error))
    
    def asignar_curso():
        try:
            select = tabla_estudiantes.focus()
            if not select:
                messagebox.showerror('¡Error¡','No hay datos seleccionados')
                return
            
            id_estudiante = tabla_estudiantes.item(select)['values'][0]
            if id_estudiante is None:
                messagebox.showerror('¡Error','Estudiante no encontrado')
                return
            
            id_curso = simpledialog.askinteger('Asignar Curso', 'Ingrese ID del Curso')            
            if id_curso is None:
                messagebox.showerror('¡Error!','Ingrese un ID valido')
                return  

            if not validar_id_curso(id_curso):
                messagebox.showerror('¡Error!','El ID Curso ingresado no existe en la Base de Datos')
                return
              
            estudiante_curso.asignar_estudiante_curso(id_estudiante, id_curso)
            actualizar_tabla()

        except ValueError:
           messagebox.showerror('¡Error!','El Estudiante ya fuye asignado a este curso')
    
    def eliminar_curso():
        try:
            select = tabla_estudiantes.focus()
            if not select:
                messagebox.showerror('¡Error!','No hay datos seleccionados')
                return
            
            values = tabla_estudiantes.item(select)['values']
            if not values:
                messagebox.showerror('¡Error!', 'No hay datos seleccionados')
                return
            
            id_estudiante = values[0]
            anio = values[6]
            division = values[7]
            orientacion = values[8]

            if anio is None or division is None or orientacion is None or anio =='None' or division == 'None' or orientacion == 'None':
                messagebox.showerror('¡Erro!','Curso inexistente')
                return

            estudiante_curso.eliminar_curso_estudiante(anio, division, orientacion,id_estudiante)
            messagebox.showinfo('Info', 'Curso eliminado correctamente')
            actualizar_tabla()
        except ValueError as error:
            print('Error al eliminar Curso'.format(error))

# ---------------- FRAME ------------
    root = tk.Tk()
    root.title('Gestion Academica')
    root.geometry('720x520')
    root.config(background='#FFFFFF')
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    root.resizable(False, False)
    root.iconbitmap('ruta del ico') #Ruta del icono

    style = ttk.Style()
    style.theme_use('default')
    style.configure('TCombobox', fieldbackground='#FFFFFF', background='#77DD77', foreground='#000000', font=('Poppins', 12))
    style.map('TCombobox', fieldbackground=[('readonly', '#FFFFFF')])
        
    datos_frame  =LabelFrame(root)
    datos_frame.grid(row=0,column=0)
    datos_frame.config(background='#FFFFFF', borderwidth=0)

    titulo = Label(datos_frame, text='Datos del Estudiante')
    titulo.grid(row=0, column=0, padx=5, pady=5, columnspan=4)
    titulo.config(font=('Poppins', 20, 'bold'), fg='#1E3A5F', bg='#FFFFFF')

    id_estudiante = Label(datos_frame,text='ID Estudiante')
    id_estudiante.grid(row=1,column=0, padx=5, pady=5, sticky='e')
    id_estudiante.config(font=('Poppins', 12, 'bold'), fg='#000000', bg='#FFFFFF')

    estudiante_entry = Entry(datos_frame)
    estudiante_entry.grid(row=1,column=1, padx=5, pady=5, sticky='w')
    estudiante_entry.config(font=('Poppins', 12), fg='#000000', bg='#FFFFFF')

    legajo = Label(datos_frame,text='Legajo')
    legajo.grid(row=2,column=0, padx=5, pady=5, sticky='e')
    legajo.config(font=('Poppins', 12, 'bold'), fg='#000000', bg='#FFFFFF')

    entry_legajo = Entry(datos_frame)
    entry_legajo.grid(row=2,column=1, padx=5, pady=5, sticky='w')
    entry_legajo.config(font=('Poppins', 12), fg='#000000', bg='#FFFFFF')

    nom_estudiante= Label(datos_frame,text='Nombre')
    nom_estudiante.grid(row=3,column=0, padx=5, pady=5, sticky='e')
    nom_estudiante.config(font=('Poppins', 12, 'bold'), fg='#000000', bg='#FFFFFF')

    campo_nom_estudiante = Entry(datos_frame)
    campo_nom_estudiante.grid(row=3, column=1, padx=5, pady=5, sticky='w')
    campo_nom_estudiante.config(font=('Poppins', 12), fg='#000000', bg='#FFFFFF')

    ape_estudiante = Label(datos_frame,text='Apellido')
    ape_estudiante.grid(row=4,column=0, padx=5, pady=5, sticky='e')
    ape_estudiante.config(font=('Poppins', 12, 'bold'), fg='#000000', bg='#FFFFFF')

    campo_ape_estudiante = Entry(datos_frame)
    campo_ape_estudiante.grid(row=4,column=1, padx=5, pady=5, sticky='w')
    campo_ape_estudiante.config(font=('Poppins', 12), fg='#000000', bg='#FFFFFF')

    sexo_estudiante=  Label(datos_frame,text='Sexo')
    sexo_estudiante.grid(row=5,column=0, padx= 5, pady=5, sticky='e')
    sexo_estudiante.config(font=('Poppins', 12, 'bold'), fg='#000000', bg='#FFFFFF')
    select_sexo = StringVar()
    combo_sexo = ttk.Combobox(datos_frame, values=['Masculino','Femenino'],textvariable=select_sexo)
    combo_sexo.grid(row=5,column=1, padx=5, pady=5, sticky='w')
    combo_sexo.set('Elige una Opcion')

    edad = [int(i) for i in range(1,50)] #creamos una lista de edades que luego mostraremos en el Combobox
    edad_estudiante = Label(datos_frame,text='Edad')
    edad_estudiante.grid(row= 6, column=0, padx=5, pady= 5, sticky='e')
    edad_estudiante.config(font=('Poppins', 12, 'bold'), fg='#000000', bg='#FFFFFF')

    combo_edad = ttk.Combobox(datos_frame,values=edad, textvariable=edad)
    combo_edad.grid(row=6,column=1, padx=5, pady=5, sticky='w')
    combo_edad.set('Selecciona una Edad') #Modificar luego la logica del bloque de codigo en la base de datos

# ------------ BOTONES -----------------

    button_guardar = Button(datos_frame,text='Guardar', command=guardar_registro, width=10, height=1)
    button_guardar.grid(row=1,column=3, columnspan=2, rowspan=1)
    button_guardar.config(font=('Poppins',10), bg='#90EE90',fg='#000000')

    button_modificar = Button(datos_frame,text='Modificar', command=modificar_registros, width=10, height=1)
    button_modificar.grid(row=2, column=3, columnspan=2, rowspan=1)
    button_modificar.config(font=('Poppins',10), bg='#90EE90',fg='#000000')

    button_eliminar = Button(datos_frame,text='Eliminar', command=eliminar_estudiante, width=10, height=1)
    button_eliminar.grid(row=3, column=3, columnspan=2, rowspan=1)
    button_eliminar.config(font=('Poppins', 10), bg='#FF6F61', fg='#000000')
    
    reset = Button(datos_frame,text='Reset',command=button_reset, width=10, height=1)
    reset.grid(row=4,column=3, columnspan=2, rowspan=1)
    reset.config(font=('Poppins', 10), bg='#FFD700', fg='#000000')

    button_asignar_curso = Button(datos_frame, text='Asignar Curso', command=asignar_curso, width=10, height=1)
    button_asignar_curso.grid(row=7, column=0, columnspan=2, padx=5, pady=5)
    button_asignar_curso.config(font=('Poppins',10), fg='#000000', bg='#90EE90')

    quitar_curso = Button(datos_frame, text='Quitar Curso', command=eliminar_curso, width=10, height=1)
    quitar_curso.grid(row=7, column=2, columnspan=2, padx=5, pady=5)
    quitar_curso.config(font=('Poppins', 10), bg='#FF6F61', fg='#000000')
   
    #------------ Treeview --------------------------

    label_listado  = LabelFrame(root)
    
    titulo_label = Label(label_listado, text='Listado de Estudiantes', font=('Poppins', 20, 'bold'), fg='#1E3A5F', bg='#FFFFFF')
    titulo_label.pack()
    label_listado.grid(row=8,column=0, padx=10, pady=10)
    label_listado.config(background='#FFFFFF', borderwidth=0)
    tabla_estudiantes = ttk.Treeview(label_listado,columns=('ID','Nombre','Apellido','Sexo','Edad','Legajo', 'Año', 'Division', 'Orientacion'),show='headings',height=5)
    tabla_estudiantes.column('#1',anchor=CENTER)
    tabla_estudiantes.heading('#1',text='ID')
    tabla_estudiantes.column('#2',anchor=CENTER,width=100)
    tabla_estudiantes.heading('#2',text='Nombre')
    tabla_estudiantes.column('#3',anchor=CENTER, width=100)
    tabla_estudiantes.heading('#3',text='Apellido')
    tabla_estudiantes.column('#4',anchor=CENTER, width=100)
    tabla_estudiantes.heading('#4',text='Sexo')
    tabla_estudiantes.column('#5',width=50, anchor=CENTER)
    tabla_estudiantes.heading('#5',text='Edad')
    tabla_estudiantes.column('# 6',anchor=CENTER, width=100)
    tabla_estudiantes.heading('# 6',text='Legajo')
    tabla_estudiantes.column('# 7',width=50, anchor=CENTER)
    tabla_estudiantes.heading('# 7',text='Año')
    tabla_estudiantes.column('# 8',width=50, anchor=CENTER)
    tabla_estudiantes.heading('# 8',text='Division')
    tabla_estudiantes.column('# 9',anchor=CENTER, width=100)
    tabla_estudiantes.heading('# 9',text='Orientacion')
    tabla_estudiantes['displaycolumns'] = (1,2,3,4,5,6,7,8)

    scroll_vertical  = Scrollbar(label_listado, orient='vertical', command=tabla_estudiantes.yview)
    tabla_estudiantes.configure(yscroll=scroll_vertical.set)
    tabla_estudiantes.pack(side='left', fill='both',expand=True)
    scroll_vertical.pack(side='right', fill='y')

    for row in conexion_estudiantes.mostrar_estudiante():
            tabla_estudiantes.insert('','end',values=row)

    tabla_estudiantes.bind("<<TreeviewSelect>>",seleccionar_registros)

    button_volver = Button(root, text='Volver', command=volver, width=10, height=1)
    button_volver.grid(row=9,column=0, pady=10, columnspan=2)
    button_volver.config(font=('Poppins',10), bg='#A4C6EB', fg='#000000')

    root.eval('tk::PlaceWindow . center')
    root.mainloop()
# interfaz_estudiantes()
