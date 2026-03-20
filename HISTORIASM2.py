inventario = []

def agregar_producto():
    """Solicita datos y los guarda en un diccionario dentro de la lista."""
    nombre = input("Nombre del producto: ")
    precio = float(input(f"Precio de {nombre}: "))
    cantidad = int(input(f"Cantidad de {nombre}: "))

    nuevo_producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad,
    }

    inventario.append(nuevo_producto)
    print("Producto registrado.")

def mostrar_inventario():
    """"Recorre la lista con un bucle for para mostrar los productos."""
    if not inventario:
        print("El inventario esta vacio.")
    else:
        for p in inventario:
            print(f"Producto: {p['nombre']} | Precio: {p['precio']} | Cantidad: {p['cantidad']}") 

def calcular_estadisticas():
    """"Calcula el valor monetario total y el numero de productos."""
    if not inventario: 
        print("No hay datos para calcular.")
        return

    valor_total = 0
    conteo_productos = len(inventario)

    for p in inventario:
        valor_total += p['precio'] * p['cantidad']

    print(f"\nTotal de productos distintos: {conteo_productos}" )
    print(f"Valor total del inventario: ${valor_total}")

def menu_principal():
    """"Mantiene el sistema activo y gestiona las opciones."""
    while True: 
        print("\n SISTEMA DE INVENTARIO")
        print("1. Agregar producto")
        print("2. Mostrar inventario")
        print("3. Calcular estadisticas")
        print("4. Salir")

        opcion = input("Seleccione una opcion: ")
        
        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            mostrar_inventario()
        elif opcion == "3":
            calcular_estadisticas()
        elif opcion == "4":
            print("Saliendo del programa...")
            break

        else:
            print("Opcion no valida, intente de nuevo.")

if __name__ == "__main__":
    menu_principal()
