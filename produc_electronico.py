

from producto import Producto

class Electronico(Producto):
    def __init__(self, nombre, precio, stock, marca, garantia_meses):
        super().__init__(nombre, precio, stock)
        self._marca = marca
        self._garantia_meses = garantia_meses

    def __str__(self):
        return f"[Electrónico] {super().__str__()} - Marca: {self._marca}, Garantía: {self._garantia_meses} meses"
