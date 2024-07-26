import tkinter as tk
from tkinter import *
from tkinter import messagebox, END, simpledialog, ttk
from connect_bd import *
from conexion_bd import *
import datos_cursos

def interfaz_profesor():
    root = tk.Tk()
    root.title('Gestion Academica')
    root.geometry('640x495')
    root.config(background='#FFFFFF')
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    root.resizable(False, False)
    root.iconbitmap('ruta del ico') #Ruta del icono

    def button_reset():
        campo_id_profesor.delete(0,END)
        campo_nombre_profesor.delete(0,END)
        campo_ap_profesor.delete(0,END)
        combo_sexo.set('Elige una Opcion')
        campo_legajo_profesor.delete(0,END)

    def cerrar_ventana():
        root.destroy()
        datos_cursos.interfaz_cursos()
    
    def guardar_registro():
        try:
            nombre = campo_nombre_profesor.get()
            apellido = campo_ap_profesor.get()
            sexo = combo_sexo.get()
            legajo = campo_legajo_profesor.get()

            if  not nombre or not apellido or not sexo or not legajo:
                messagebox.showerror('¡Error!',' Completa todos los campos')
                return
            if not validar_combo_sexo():
                messagebox.showerror('¡Error!', 'Seleccione un sexo valido')
                return
            try: 
                datos_profesor.carga_datos_profesor(nombre,apellido,sexo,legajo)
                messagebox.showinfo('Info','Los datos fueron guardados')
            except ValueError as error:
                messagebox.showerror('¡Error!', str(error))
                return
            except Exception as error:
                messagebox.showerror('¡Error!','No se pudo insertar el legajo en la Base de Datos')
                return
            actualizar_tabla()

            campo_nombre_profesor.delete(0,END)
            campo_ap_profesor.delete(0,END)
            combo_sexo.set('Elige una Opcion')
            campo_legajo_profesor.delete(0,END)

        except ValueError as error:
            print('Error al ingresar los datos'.format(error))
            messagebox.showerror('¡Error!','Error al ingresar los datos')

    def actualizar_tabla():
        try:
            tabla_profesor.delete(*tabla_profesor.get_children())
            datos = datos_profesor.mostrar_profesor()
            for row in datos:
                tabla_profesor.insert('','end',values=row)
        except ValueError as error:
            print('Error al actualizar tabla'.format(error))   

    def seleccionar_registros(evento): 
        try:
            select = tabla_profesor.focus()
            
            if select:
                values = tabla_profesor.item(select)['values']
                campo_id_profesor.delete(0,END)
                campo_id_profesor.insert(0,values[0])
                campo_nombre_profesor.delete(0,END)
                campo_nombre_profesor.insert(0,values[1])
                campo_ap_profesor.delete(0,END)
                campo_ap_profesor.insert(0,values[2])
                combo_sexo.set(values[3])
                campo_legajo_profesor.delete(0,END)
                campo_legajo_profesor.insert(0,values[4])
        except ValueError as error:
            print('Error al seleccionar registro'.format(error))   

    def modificar_registro():
        try:
            idusuario = campo_id_profesor.get()
            nombre = campo_nombre_profesor.get()
            apellido = campo_ap_profesor.get()
            sexo = combo_sexo.get() 
            legajo = campo_legajo_profesor.get()

            if not idusuario or not nombre or not apellido or not sexo or not legajo:
                messagebox.showerror('¡Error!','Los valores no estan inicalizados')
                return
             
            if not validar_combo_sexo():
                messagebox.showerror('¡Error!','Ingrese un sexo valido')
                return

            if not validar_legajo(legajo):
                messagebox.showerror('¡Error!','Ingrese un legajo valido')
                return
            
            datos_profesor.modificar_profesor(idusuario,nombre,apellido,sexo,legajo)
            messagebox.showinfo('Info','Los datos fueron actualizados')

            actualizar_tabla()

            campo_id_profesor.delete(0,END)
            campo_nombre_profesor.delete(0,END)
            campo_ap_profesor.delete(0,END)
            combo_sexo.delete(0,END)
            campo_legajo_profesor.delete(0,END)

        except ValueError as error:
            print('Error al modificar los datos'.format(error))  

    def eliminar_registros():
        try:
            idusuario = campo_id_profesor.get()
            if not idusuario:
                messagebox.showerror('¡Error!','Los valores no estan inicalizados')
                return
                    
            datos_profesor.eliminar_profesor(idusuario)
            messagebox.showinfo('Info','Los datos fueron eliminados')

            actualizar_tabla()

            campo_id_profesor.delete(0,END)
            campo_nombre_profesor.delete(0,END)
            campo_ap_profesor.delete(0,END)
            campo_legajo_profesor.delete(0,END)
            combo_sexo.set('Elige una opcion')

        except ValueError as error:
            print('Error al eliminar los datos'.format(error)) 

    def asignar_curso():
        try:
            select = tabla_profesor.focus()
            if not select:
                messagebox.showerror('¡Error!','No hay datos seleccionados')
                return
            
            id_profesor = tabla_profesor.item(select)['values'][0]
            if not id_profesor:
                messagebox.showerror('¡Error!','Profesor no encontrado')
                return
            
            id_curso = simpledialog.askinteger('Asignar curso', 'Ingrese ID del Curso')
            if not id_curso :
                messagebox.showerror('¡Error!','Ingrese un ID valido')
                return
            if not validar_id_curso(id_curso):
                messagebox.showerror('¡Error!','El ID Curso ingresado no existe en la Base de Datos')
                return
            
            profesor_curso.asignar_profesor_curso(id_profesor, id_curso)
            messagebox.showinfo('Info','Profesor asignado correctamente')
            root.destroy()
            datos_cursos.interfaz_cursos() 
            
        except ValueError:
            messagebox.showerror('¡Error!','El Profesor ya fue asignado a este curso')
            return
    
    def validar_combo_sexo():
        if select_sexo.get() not in ['Masculino','Femenino']:
            return False
        return True

#--------------- ENTRADAS Y ETIQUETAS -------------------

    style = ttk.Style()
    style.theme_use('default')
    style.configure('TCombobox', fieldbackground='#FFFFFF', background='#77DD77', foreground='#000000', font=('Poppins', 12))
    style.map('TCombobox', fieldbackground=[('readonly', '#FFFFFF')])
    
    datos_labelframe = LabelFrame(root)
    datos_labelframe.grid(row=0,column=0,padx=5,pady=5)
    datos_labelframe.config(background='#FFFFFF', borderwidth=0)

    datos = Label(datos_labelframe, text='Datos del Profesor')
    datos.grid(row=0, column=0, padx=5, pady=5, columnspan=3)
    datos.config(font=('Poppins', 20, 'bold'), fg='#1E3A5F', bg='#FFFFFF')
        
    id_profesor = Label(datos_labelframe,text='ID')
    id_profesor.grid(row=1,column=0, padx=5, pady=5, sticky='e')
    id_profesor.config(font=('Poppins', 12, 'bold'), fg='#000000', bg='#FFFFFF')

    campo_id_profesor = Entry(datos_labelframe)
    campo_id_profesor.grid(row=1,column=1, padx=5, pady=10, sticky='w')
    campo_id_profesor.config(font=('Poppins', 12), fg='#000000', bg='#FFFFFF')

    legajo_profesor = Label(datos_labelframe,text='Legajo')
    legajo_profesor.grid(row=2, column=0, padx=5, pady=5, sticky='e')
    legajo_profesor.config(font=('Poppins', 12, 'bold'), fg='#000000', bg='#FFFFFF')

    campo_legajo_profesor= Entry(datos_labelframe)
    campo_legajo_profesor.grid(row=2,column=1, padx=5, pady=5, sticky='w')
    campo_legajo_profesor.config(font=('Poppins', 12), fg='#000000', bg='#FFFFFF')

    nom_profesor = Label(datos_labelframe,text='Nombre')
    nom_profesor.grid(row=3,column=0, padx=5, pady=5, sticky='e')
    nom_profesor.config(font=('Poppins', 12, 'bold'), fg='#000000', bg='#FFFFFF')

    campo_nombre_profesor = tk.Entry(datos_labelframe)
    campo_nombre_profesor.grid(row=3,column=1, padx=5, pady=5, sticky='w')
    campo_nombre_profesor.config(font=('Poppins', 12), fg='#000000', bg='#FFFFFF')

    ape_profesor = Label(datos_labelframe,text='Apellido')
    ape_profesor.grid(row=4,column=0, padx=5, pady=5, sticky='e')
    ape_profesor.config(font=('Poppins', 12, 'bold'), fg='#000000', bg='#FFFFFF')

    campo_ap_profesor = Entry(datos_labelframe)
    campo_ap_profesor.grid(row=4,column=1, padx=5, pady=5, sticky='w')
    campo_ap_profesor.config(font=('Poppins', 12), fg='#000000', bg='#FFFFFF')

    sexo_profesor = Label(datos_labelframe,text='Sexo')
    sexo_profesor.grid(row=5,column=0, padx=5, pady=5, sticky='e')
    sexo_profesor.config(font=('Poppins', 12, 'bold'), fg='#000000', bg='#FFFFFF')

    select_sexo = tk.StringVar()
    combo_sexo = ttk.Combobox(datos_labelframe,values=['Masculino','Femenino'],textvariable=select_sexo, style='TCombobox')
    combo_sexo.grid(row=5,column=1, padx=5, pady=5, sticky='w')
    select_sexo.set('Elige una Opcion')

    #------------------- BOTONES ------------------------

    button_guardar = Button(datos_labelframe,text='Guardar',command=guardar_registro, width=10, height=1)
    button_guardar.grid(row=1,column=2,rowspan=2, padx=10, pady=15)
    button_guardar.config(font=('Poppins', 10), fg='#000000', bg='#90EE90')

    button_modificar = Button(datos_labelframe,text='Modificar',command=modificar_registro, width=10, height=1)
    button_modificar.grid(row=2,column=2, rowspan=2, padx=10, pady=10)
    button_modificar.config(font=('Poppins', 10), fg='#000000', bg='#90EE90')

    button_eliminar = Button(datos_labelframe,text='Eliminar', command=eliminar_registros, width=10, height=1)
    button_eliminar.grid(row=3,column=2, rowspan=2, padx=10, pady=15)
    button_eliminar.config(font=('Poppins', 10), fg='#000000', bg='#FF6F61')

    button_asignar = Button(datos_labelframe,text='Asignar Curso',command=asignar_curso, width=15, height=1)
    button_asignar.grid(row=6,column=0, columnspan=2, padx=10, pady=10)
    button_asignar.config(font=('Poppins', 10), fg='#000000', bg='#90EE90')

    reset_button = Button(datos_labelframe,text='Reset',command=button_reset, width=10, height=1)
    reset_button.grid(row=6,column=2, columnspan=2, padx=10, pady=10)
    reset_button.config(font=('Poppins', 10), fg='#000000', bg='#FFD700')

# ------------------------Treeview-----------------------
 
    datos_labelframe1 = LabelFrame(root)

    titulo = Label(datos_labelframe1, text='Listado de Profesor',font=('Poppins', 19, 'bold'), fg='#1E3A5F', bg='#FFFFFF')
    titulo.pack()

    datos_labelframe1.grid(row=7, column=0, padx=5, pady=5)
    datos_labelframe1.config(background='#FFFFFF', borderwidth=0)
    tabla_profesor = ttk.Treeview(datos_labelframe1, columns=('ID','Nombre','Apellido','Sexo','Legajo'),show='headings',height=5,)
    tabla_profesor.column('# 1',anchor=CENTER)
    tabla_profesor.heading('# 1 ',text='ID')
    tabla_profesor.column('# 2',anchor=CENTER, width=150)
    tabla_profesor.heading('# 2 ',text='Nombre')
    tabla_profesor.column('# 3',anchor=CENTER, width=150)
    tabla_profesor.heading('# 3 ',text='Apellido')
    tabla_profesor.column('# 4',anchor=CENTER, width=150)
    tabla_profesor.heading('# 4 ',text='Sexo')
    tabla_profesor.column('# 5',anchor=CENTER, width=150)
    tabla_profesor.heading('# 5 ',text='Legajo')
    tabla_profesor['displaycolumns'] = (1,2,3,4)
    scroll_vertical = Scrollbar(datos_labelframe1, orient='vertical', command=tabla_profesor.yview)
    tabla_profesor.configure(yscroll=scroll_vertical.set)
    tabla_profesor.pack(side='left', fill='both', expand=True)
    scroll_vertical.pack(side='right', fill='y') 

    for row in datos_profesor.mostrar_profesor():
        tabla_profesor.insert('','end',values=row)

    tabla_profesor.bind("<<TreeviewSelect>>",seleccionar_registros)

    button_volver = Button(root,text='Volver',command=cerrar_ventana, width=10, height=1)
    button_volver.grid(row=8,column=0,pady=10, columnspan=2)
    button_volver.config(font=('Poppins',10), bg='#A4C6EB', fg='#000000')
    
    root.eval('tk::PlaceWindow . center')
    root.mainloop()

# interfaz_profesor()
