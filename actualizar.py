from mostrar import mostrar_inventario
producto = ""
valor = 0

def actuazlizar_producto(inventario):
    producto = input("Ingrese el producto: ")
    try:
        if producto in inventario:
            valor = float(input("Ingrese la cantidad  actualizar: "))
            print(f"actualizando stock de {producto} a {valor}.\n")
            inventario[producto] = valor
            mostrar_inventario(inventario)
        else:
            print("El producto no existe")
    except ValueError: 
        print("no se encuentra el producto") 