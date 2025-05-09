from mostrar import mostrar_inventario
from actualizar import actualizar_producto

#inventario inicial
from agregar import agregar
from eliminar import eliminar

inventario = {
    'manzanas': 50,
    'naranjas': 30,
    'peras': 20
}

mostrar_inventario(inventario)
actualizar_producto(inventario)
agregar(inventario)
eliminar(inventario)
