producto = ""
valor = 0

def mostrar_inventario(inventario):
    print("**********Inventario actual**********")

    for producto, valor in inventario.items():
        print(f"-{producto}: {valor}")