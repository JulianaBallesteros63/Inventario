# alimento.py

from producto import Producto

class Alimento(Producto):
    def __init__(self, nombre, precio, stock, fecha_expiracion):
        super().__init__(nombre, precio, stock)
        self._fecha_expiracion = fecha_expiracion

    def __str__(self):
        return f"[Alimento] {super().__str__()} - Expira: {self._fecha_expiracion}"
