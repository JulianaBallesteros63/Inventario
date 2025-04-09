

class Producto:
    def __init__(self, nombre, precio, stock):
        self._nombre = nombre
        self._precio = precio
        self._stock = stock

    def __str__(self):
        return f"{self._nombre} - ${self._precio} ({self._stock} unidades disponibles)"

    def actualizar_stock(self, cantidad):
        self._stock += cantidad

    def obtener_precio(self):
        return self._precio
