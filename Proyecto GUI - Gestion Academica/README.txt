*****************************************************************************************************************************************
* REQUISITOS PARA CORRER EL PROGRAMA GESTION ACADEMICA (Solo Windows 10, No testeado en Windows 11)				 	*
*****************************************************************************************************************************************
* INSTALAR LAS LIBRERIAS NECESARIAS DE PYTHON ---| TKINTER Y MYSQL.CONNECTOR |---						 	*
* pip install tk <--- tkinter													 	*
* pip install mysql-connector-python <--- mysql.connector										*
* imagenes del programa en la carpeta 'GALERIA'									 			*
*****************************************************************************************************************************************
* 1) TENER EL GESTOR DE BASE DE DATOS INSTALADO EN EL SISTEMA (MySQL Workbench)								*
*	> Abrir el archivo gestion_academica.sql con el gestor BD (MySQL Workbench)							*
*	> El archivi gestion_academica.sql contiene todas las tablas y relaciones creadas 						*								 	*
* 2) CAMBIAR LAS CREDENCIALES DE ACCESO (usuario, contraseña, puerto y host) POR SUS PROPIAS CREDENCIALES EN EL MODULO conexion_bd.py 	*
*	> Una vez reemplazada las credenciales ejecutar el modulo conexion_bd.py y debe mostrar el siguiente mensaje: True	 	*
*	> Si la Conexion a la Base de Datos se hizo correctamente le saldra un mensaje de "True" sino "False"			 	*
* 3) EN EL MODULO main.py REEMPLAZAR LA RUTA DE CARPETA DEL ARCHIVO ico, img							 	*
*	> Ejemplo --> 'D:\Gestion Academica\ico\ico.ico' o 'D:\Gestion Academica\img\logo2.png'					 	*
* 4) REPETIR EL PASO (3) PARA REEMPLAZAR LA RUTA DEL ICO EN LOS MODULOS: datos_cursos.py, datos_estudiantes.py, datos_profesor.py 	*
* 5) 				!!!A DISFRUTAR DEL PROGRAMA¡¡¡¡¡								 	*
*****************************************************************************************************************************************