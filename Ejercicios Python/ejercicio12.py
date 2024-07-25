# Cálculo de descuento: 
# Crea una función que calcule el precio final después de aplicar un descuento dado a un producto. 
# La función debe aceptar el precio original y el porcentaje de descuento como argumentos.

def descuento(precio_original, porcentaje_descuento):
    total_descuento = precio_original - ( precio_original * porcentaje_descuento/100)
    return total_descuento

print(descuento(1200, 10)) # resultado --> 1080.0
print(descuento(1500, 30)) # resultado --> 1050.0
