producto = ""
valor = 0

def agregar (inventario):
    producto = input("Ingrese el producto: ")
    valor = float(input("Ingrese la cantidad: "))
    inventario[producto] = valor

    print(inventario)
