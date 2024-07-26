import tkinter as tk
from tkinter import messagebox
import datos_cursos
from tkinter import *

def registrar_usuario():
        user = campo_user.get()
        passw = campo_pass.get()
        if not user or not passw:  #Verifica si los campos estan vacios, y muestra mensaje de error
            messagebox.showerror('¡Error!', 'Por favor, complete todos los campos') # ejemplo del messagebox
            return
        elif user =='admin' and passw == 'admin':
            messagebox.showinfo('Inicio de Sesion','¡Has iniciado sesion correctamente!') #Muestra mensaje de exito
            cerrar_ventana()
            datos_cursos.interfaz_cursos()
        else: 
            user != 'admin' and passw != 'admin'
            messagebox.showerror('¡Error!','Los datos no coinciden')

def cerrar_ventana():
        root.destroy()

root = tk.Tk()
root.title('Gestion Academica') #Titulo de ventana
root.geometry('400x430') #Tamaño de Ventana Principal
root.config(bg='#FFFFFF') # Fondo Blanoco
root.columnconfigure(0, weight=1) 
root.rowconfigure(0, weight=1)
root.resizable(False, False)
root.iconbitmap('Ruto del ico') #Ruta del icono
img = tk.PhotoImage(file='Ruta de la imagen') #Ruta img

registro_label = LabelFrame(root)
registro_label.grid(row=0, column=0, padx=40, pady=40)
registro_label.config(font=('San-Serif', 12), background='#FFFFFF', borderwidth=0)
# ---- IMAGE ------
image_label= Label(registro_label, image=img, bg='#FFFFFF', width=150, height=150)
image_label.grid(row=0,column=0, padx=5, pady=5, columnspan=3)

inicio_sesion = Label(registro_label, text='Inicio de Sesion')
inicio_sesion.grid(row=1,column=0, padx=5,pady=5,columnspan=2)
inicio_sesion.config(font=('Poppins', 20, 'bold'), fg='#1E3A5F', bg='#FFFFFF')
# ------------ USUARIO -----------------
label_user = Label(registro_label,text='Usuario')
label_user.grid(row=2, column=0,padx=(10,5),pady=10, sticky='e')
label_user.config(font=('Poppins',12, 'bold'), fg= '#000000', bg='#FFFFFF')
campo_user = Entry(registro_label)
campo_user.grid(row=2,column=1, padx=(5,10), pady=10, sticky='w')
campo_user.config(font=('Poppins',12), fg= '#000000', bg='#FFFFFF')
# --------------- Contraseña ---------
label_pass = Label(registro_label,text='Contraseña')
label_pass.grid(row=3, column=0, padx=(10,5), pady=10, sticky='e')
label_pass.config(font=('Poppins',12, 'bold'), fg= '#000000', bg='#FFFFFF')
campo_pass = Entry(registro_label,show='*')
campo_pass.grid(row=3, column=1, padx=(5,10), pady=10, sticky='w')
campo_pass.config(font=('Poppins',12), fg= '#000000', bg='#FFFFFF')

#Definimos botones  para acceder/salir

button_register = Button(registro_label,text='Acceder',command=registrar_usuario, width=10, height=1, cursor='hand2')
button_register.grid(row=4, column=1, columnspan=1, padx=(5,10), pady=5, sticky='e')
button_register.config(bg='#77DD77', font=('Poppins',10), fg= '#000000')

button_salir = Button(registro_label, text='Salir',command=cerrar_ventana, width=10, height=1, cursor='hand2')
button_salir.grid(row=4, column=0, columnspan=2, padx=(10,5), pady=5, sticky='w')
button_salir.config(bg='#FF6F61', font=('Poppins', 10), fg= '#000000')

root.eval('tk::PlaceWindow . center')
root.mainloop()
