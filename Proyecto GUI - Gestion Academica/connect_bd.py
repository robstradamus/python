from conexion_bd import *

def validar_legajo(legajo):
        if len(legajo)!=4:
            return False
        if not legajo.isdigit():
            return False
        return True

def validar_id_curso(id_curso):
    try:
        # conexion = Conexion_BD.conexion_bd()
        conexion = Conexion_BD()
        if conexion is None:
            return False
        # cursor = conexion.cursor()
        conexion.cursor.execute('select count(*) from tabla_cursos where id_curso = %s;',(id_curso,))
        resultado = conexion.cursor.fetchone()
        # conexion.close()
        return resultado[0]>0
    except mysql.connector.Error as error:
        print('Error al validar ID Curso'.format(error))

def validar_id_profesor(id_profesor):
    try:
        # conexion = Conexion_BD.conexion_bd()
        conexion = Conexion_BD()
        if conexion is None:
            return False
        cursor = conexion.cursor()
        conexion.cursor.execute('select count(*) from tabla_profesor where id_profesor = %s;',(id_profesor,))
        resultado = conexion.cursor.fetchone()
        # conexion.close()
        return resultado[0]>0
    except mysql.connector.Error as error:
        print('Error al validar ID Profesor'.format(error))

def validar_id_estudiante(id_estudiante):
    try:
        # conexion = Conexion_BD.conexion_bd()
        conexion = Conexion_BD()
        if conexion is None:
            return False 
        cursor = conexion.cursor()
        conexion.cursor.execute('select count(*) from tabla_estudiante where id_estudiante = %s;',(id_estudiante,))
        resultado = conexion.cursor.fetchone()
        # conexion.close()
        return resultado[0]>0
    except mysql.connector.Error as error:
        print('Error al validar ID Estudiante'.format(error))

# Modificado
class datos_profesor:

    def carga_datos_profesor(nombre,apellido,sexo,legajo):
        
        if not validar_legajo(legajo):
                raise ValueError ("¡Error!","Legajo no valido. Debe tener 4 digitos")
        
        try:
            # conexion = Conexion_BD.conexion_bd()
            # cursor = conexion.cursor()
            conexion.cursor.execute("SELECT COUNT(*) FROM tabla_profesor WHERE legajo = %s", (legajo,))
            if conexion.cursor.fetchone()[0] > 0:
                raise ValueError("El legajo ya existe en la base de datos.")
            
            sql = 'insert into tabla_profesor values(null,%s,%s,%s,%s);' #<<-- carga de valores en la BD
            valores = (nombre,apellido,sexo,legajo)
            conexion.cursor.execute(sql,valores)
            conexion.commit() 
            print(conexion.cursor.rowcount,'Registro Ingresado')
            # conexion.close()
                    
        except mysql.connector.Error as error:
            print('Error de ingresos de datos'.format(error))
# modificado
    def mostrar_profesor(): 
        try:
            # conexion = Conexion_BD.conexion_bd()
            # conexion = Conexion_BD()
            # cursor = conexion.cursor()
            conexion.cursor.execute("select * from tabla_profesor;")
            mi_consulta = conexion.cursor.fetchall()
            conexion.commit()
            # conexion.conexion.close()
            return mi_consulta
        
        except mysql.connector.Error as error:
            print('Error al mostrar Datos'.format(error))

    def modificar_profesor(id_profesor,nombre,apellido,sexo,legajo):
        try:
            # conexion = Conexion_BD.conexion_bd()
            # cursor = conexion.cursor()
            sql = 'update tabla_profesor set nombre_profesor = %s, apellido_profesor = %s, genero_profesor = %s, legajo = %s where id_profesor = %s;' #<<-- carga de valores en la BD
            valores = (nombre,apellido,sexo,legajo,id_profesor)
            conexion.cursor.execute(sql,valores)
            conexion.commit() 
            print(conexion.cursor.rowcount,'Registro Actualizado')
            # conexion.close()
                    
        except mysql.connector.Error as error:
            print('Error de actualizacion'.format(error))
    
    def eliminar_profesor(id_profesor):
        try:
            # conexion = Conexion_BD.conexion_bd()
            # cursor = conexion.cursor()
            sql = 'delete from tabla_profesor where id_profesor = %s' #<<-- carga de valores en la BD
            valores = (id_profesor,)
            conexion.cursor.execute(sql,valores)
            conexion.commit() 
            print(conexion.cursor.rowcount,'Registro Eliminado')
            # conexion.close()
                    
        except mysql.connector.Error as error:
            print('Error al eliminar registro'.format(error))

class conexion_estudiantes:

    def carga_datos(nombre,apellido,sexo,edad,legajo):
        if not validar_legajo(legajo):
                raise ValueError ('¡Error!','Legajo no valido. Debe tener 4 digitos')
        try:
            # conexion = Conexion_BD.conexion_bd()
            # cursor = conexion.cursor()
            conexion.cursor.execute("SELECT COUNT(*) FROM tabla_estudiante WHERE legajo = %s", (legajo,))
            if conexion.cursor.fetchone()[0] > 0:
                raise ValueError("El legajo ya existe en la base de datos.")
                
            sql = 'insert into tabla_estudiante values(null,%s,%s,%s,%s,%s);'
            valores = (nombre,apellido,sexo,edad,legajo)
            conexion.cursor.execute(sql,valores)
            conexion.commit()
            print(conexion.cursor.rowcount,'Registro Ingresado')
            # conexion.close()

        except mysql.connector.Error as error:
            print('Error al ingresar datos'.format(error))

    def mostrar_estudiante():
        try:
            # conexion = Conexion_BD.conexion_bd()
            # cursor = conexion.cursor()
            conexion.cursor.execute('SELECT  e.id_estudiante, e.nombre_estudiante, e.apellido_estudiante, e.genero_estudiante, e.edad, e.legajo,c.anio, c.division, c.orientacion FROM tabla_estudiante e LEFT JOIN estudiante_curso ec ON e.id_estudiante = ec.estudiante_id LEFT JOIN  tabla_cursos c ON ec.curso_id = c.id_curso;')
            mi_consulta = conexion.cursor.fetchall()
            conexion.commit()
            # conexion.close()
            return mi_consulta
        
        except mysql.connector.Error as error:
            print('Error al mostrar los datos'.format(error))
    
    def modificar_estudiante(id_estudiante,nombre,apellido,sexo,edad,legajo):
        try:
            # conexion = Conexion_BD.conexion_bd()
            # cursor = conexion.cursor()
            sql = 'update tabla_estudiante set nombre_estudiante = %s, apellido_estudiante = %s, genero_estudiante = %s, edad = %s, legajo = %s where id_estudiante = %s;'
            valores=(nombre,apellido,sexo,edad,id_estudiante,legajo)
            conexion.cursor.execute(sql,valores)
            conexion.commit()
            print(conexion.cursor.rowcount,'Registro actualizado')
            # conexion.close()
        except mysql.connector.Error as error:
            print('Error al modificar datos'.format(error))
    
    def eliminar_estudiante(id_estudiante):
        try:
            # conexion = Conexion_BD.conexion_bd()
            # cursor = conexion.cursor()
            sql = 'delete from tabla_estudiante where id_estudiante = %s;'
            valores=(id_estudiante,)
            conexion.cursor.execute(sql,valores)
            conexion.commit()
            print(conexion.cursor.rowcount,'Registro eliminado correctamente')
            # conexion.close()

        except mysql.connector.Error as error:
            print('Error al eliminar registro'.format(error))

class conexion_curso:

    def carga_datos_curso(year,division,orientacion):
        try:
            # conexion = Conexion_BD.conexion_bd()
            # cursor = conexion.cursor()
            sql = 'insert into tabla_cursos values(null,%s,%s,%s);'
            valores = (year,division,orientacion)
            conexion.cursor.execute(sql,valores)
            conexion.commit()
            print(conexion.cursor.rowcount,'Registro ingresados')
            # conexion.close()
        except mysql.connector.Error as error:
            print('Error al ingresar datos'.format(error))
    
    def mostrar_curso():
        try:
            # conexion = Conexion_BD.conexion_bd()
            # cursor = conexion.cursor()
            conexion.cursor.execute('SELECT c.id_curso, c.anio, c.division, c.orientacion, p.nombre_profesor as profesor from tabla_cursos c left join profesor_cursos pc on c.id_curso = pc.curso_id left join tabla_profesor p on pc.profesor_id = p.id_profesor;')
            mi_consulta = conexion.cursor.fetchall()
            conexion.commit()
            # conexion.close()
            return mi_consulta
        except mysql.connector.Error as error:
            print('Error al mostrar los datos'.format(error))
    
    def modificar_curso(id_curso,year,division,orientacion):
        try:
            # conexion = Conexion_BD.conexion_bd()
            # cursor = conexion.cursor()
            sql = 'update tabla_cursos set anio = %s, division = %s, orientacion = %s where id_curso = %s;'
            valores = (year,division,orientacion,id_curso)
            conexion.cursor.execute(sql,valores)
            conexion.commit()
            print(conexion.cursor.rowcount,'Registro actualizado')
            # conexion.close()
        except mysql.connector.Error as error:
            print('Error al actualizar registro'.format(error))
    
    def eliminar_curso(id_curso):
        try:
            # conexion = Conexion_BD.conexion_bd()
            # cursor = conexion.cursor()
            sql = 'delete from tabla_cursos where id_curso = %s'
            valores = (id_curso,)
            conexion.cursor.execute(sql,valores)
            conexion.commit()
            print(conexion.cursor.rowcount,'Registro eliminado correctamente')
            # conexion.close()
        except mysql.connector.Error as error:
            print('Error al eliminar registro'.format(error))

# ------- conexion de profesor_curso -------

class profesor_curso:
    def asignar_profesor_curso(id_profesor,id_curso):
        try:
            # conexion = Conexion_BD.conexion_bd()
            # cursor = conexion.cursor()
            conexion.cursor.execute('select count(*) from profesor_cursos where profesor_id = %s and curso_id = %s;',(id_profesor, id_curso))
            if conexion.cursor.fetchone()[0]>0:
                raise ValueError('¡Error!','El Profesor ya fue asignado a este curso')
            sql = 'insert into profesor_cursos (profesor_id, curso_id) values(%s, %s);'
            valores = (id_profesor, id_curso)
            conexion.cursor.execute(sql, valores)
            conexion.commit()
            print(conexion.cursor.rowcount, 'Curso actualizado con profesor')
            # conexion.close()
        except mysql.connector.Error as error:
            print('Error al asignar profesor al curso:', error)

    def eliminar_profesor(profesor_id,curso_id):
        try:
            # conexion = Conexion_BD.conexion_bd()
            # cursor = conexion.cursor()
            sql='delete from profesor_cursos where profesor_id = (select id_profesor from tabla_profesor where nombre_profesor = %s) and curso_id = %s;'
            valores=(profesor_id,curso_id)
            conexion.cursor.execute(sql,valores)
            conexion.commit()
            print(conexion.cursor.rowcount, 'Profesor eliminado del curso')
            # conexion.close()
        except mysql.connector.Error as error:
            print('Error al quitar profesor del curso')

# --------- conexion estudiante_curso --------------

class estudiante_curso:

    def asignar_estudiante_curso(id_estudiante, id_curso):
        try: 
            # conexion = Conexion_BD.conexion_bd()
            # cursor = conexion.cursor()
            conexion.cursor.execute('select count(*) from estudiante_curso where estudiante_id = %s and curso_id = %s;',(id_estudiante, id_curso))
            if conexion.cursor.fetchone()[0]>0:
                raise ValueError('¡Error!','El Estudiante ya fue asignado a este curso')
            
            sql = 'insert into estudiante_curso (estudiante_id, curso_id) values(%s, %s);'
            valores = (id_estudiante, id_curso)
            conexion.cursor.execute(sql,valores)
            conexion.commit()
            print(conexion.cursor.rowcount,'Curso actualizado con Estudiante')
            # conexion.close()
        except mysql.connector.Error as error:
            print('Error al agregar estudiantes al curso'.format(error))
    
    def eliminar_curso_estudiante(anio, division, orientacion, id_estudiante):
        try:
            # conexion = Conexion_BD.conexion_bd()
            # cursor = conexion.cursor()
            sql = 'DELETE FROM estudiante_curso WHERE curso_id = (SELECT id_curso FROM tabla_cursos WHERE anio = %s AND division = %s AND orientacion = %s) AND estudiante_id = %s;'
            valores = (anio, division, orientacion, id_estudiante)
            conexion.cursor.execute(sql, valores)
            conexion.commit()
            print(conexion.cursor.rowcount, 'Curso Eliminado')
            # conexion.close()
        except mysql.connector.Error as error:
            print('Error al eliminar curso')
