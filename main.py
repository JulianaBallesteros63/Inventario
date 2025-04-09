# este es el cambio de jhon jairo 
import sys
import os
sys.path.append(os.path.dirname(__file__))

from produc_electronico import Electronico
from alimento import Alimento

# Funciones para crear productos
def crear_electronico():
    nombre1 = input("Nombre del producto electrónico: ")
    precio = float(input("Precio: "))
    stock = int(input("Cantidad en stock: "))
    marca = input("Marca: ")
    garantia = int(input("Garantía (en meses): "))
    return Electronico(nombre1, precio, stock, marca, garantia)

def crear_alimento():
    nombre2 = input("Nombre del alimento: ")
    precio = float(input("Precio: "))
    stock = int(input("Cantidad en stock: "))
    fecha_cad = input("Fecha de caducidad (YYYY-MM-DD): ")
    return Alimento(nombre2, precio, stock, fecha_cad)

# Crear productos
print("=== Crear producto electrónico ===")
e1 = crear_electronico()

print("\n=== Crear alimento ===")
a1 = crear_alimento()

# Mostrar productos
print("\n=== Productos creados ===")
print(e1)
print(a1)

# Actualizar stock
cantidad = int(input(f"\n¿Cuánto deseas modificar el stock de {e1}? (+ o -): "))
e1.actualizar_stock(cantidad)

# Actualizar stock
cantidad = int(input(f"\n¿Cuánto deseas modificar el stock de {a1}? (+ o -): "))
a1.actualizar_stock(cantidad)

print("\nStock actualizado:", e1)
print("\nStock actualizado:", a1)


