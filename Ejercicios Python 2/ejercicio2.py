# Gestión de Inventario:
# Crea un programa que mantenga un inventario de productos utilizando un diccionario, 
# donde las llaves sean los nombres de los productos y los valores sean las cantidades disponibles de cada producto.

inventario = {}

def mostrar_inverntario(inventario):
    print('Inventario Actual: ')
    for productos, cantidad in inventario.items():
        print(productos,':',cantidad)
    print()
def agregar_producto(inventario, productos, cantidad):
    if productos in inventario:
        inventario[productos] += cantidad
    else:
        inventario[productos] = cantidad

def actualizar_cantidad(inventario, productos, cantidad):
    if productos in inventario:
        inventario[productos] = cantidad

def eliminar_producto(inventario, producto):
    if producto in inventario:
        del inventario[producto]
        print(producto,'eliminado del inventario')
    else:
        print(producto,'no se encuentra en el inventario')

# Ejemplos
agregar_producto(inventario,'Manzana',50)
agregar_producto(inventario,'Banana',30)
agregar_producto(inventario,'Naranja',10)
mostrar_inverntario(inventario)

actualizar_cantidad(inventario, 'Manzana', 100)
mostrar_inverntario(inventario)

eliminar_producto(inventario, 'Naranja')
mostrar_inverntario(inventario)