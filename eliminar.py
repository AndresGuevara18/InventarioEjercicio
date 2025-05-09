producto = ""
valor = 0


def eliminar (inventario):
    producto = input("Ingrese las fruta a elimimar: ").lower()
    if producto in inventario:
        del inventario[producto]
        print(f"EL producto {producto} fue eliminado")
    else:
        print("El producto no existe")

    print(inventario)