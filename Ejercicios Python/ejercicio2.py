# Validación de contraseña: Crea una función que valide una contraseña según ciertas condiciones 
# (por ejemplo, debe tener al menos 8 caracteres, contener al menos una letra mayúscula y un número). 
# La función deberá devolver True si la contraseña es válida y False en caso contrario.


def validar_password(password):
    if len(password) < 8: # Verifica que la longuitud sea al menos de 8 caracteres
        return False
     
    mayus = False # Inicializar bool para las condiciones
    num = False 

    for pwd in password: # Verifica cada caracter de la contraseña
        if pwd.isdigit():
            return True
        if pwd.isupper():
            return True
        if mayus and num: # Cierra bucle si ambas condiciones se cumplen
            break
    # Verifica que todas las condiciones se cumplan   
    if mayus and num:
        return True


print(validar_password('Contraseña1')) # True
print(validar_password('Pass')) # False

    