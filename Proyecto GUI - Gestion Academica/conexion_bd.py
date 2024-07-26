import mysql.connector
import os

class Conexion_BD:
      def __init__(self):
             self.conexion = mysql.connector.connect(
                 user="usuario",
                 password = "contraseña",
                 host = "localhost", #No es necesario Modificar y que lo corre desde una maquina local, sino reemplazar por la direccion IP del localhost
                 database = "gestion_academica", #Nombre de la Base de Datos, en caso de haber modificado el nombre de la BD reemplazar por el nombre correspondiente
                 port = "3306") #El Puerto del Gestor BD, reemplazar si tienes otro Puerto
             
             self.cursor = self.conexion.cursor()
             print("La base de datos consultada es:", self.conexion.database)
             
            
      def commit(self):
          self.conexion.commit()      

conexion = Conexion_BD()
print(type(conexion))
print(hasattr(conexion, 'cursor'))
