class Prenda:

    def __init__(self, id_prenda, nombre, tipo, color, talla, precio, cantidad):
        self.id_prenda = id_prenda
        self.nombre = nombre
        self.tipo = tipo
        self.color = color
        self.talla = talla
        self.precio = precio
        self.cantidad = cantidad

    def mostrar_info(self):
        print(f"  [{self.id_prenda}] {self.nombre} | {self.tipo} | {self.color} | {self.talla} | ${self.precio:,.0f} | Stock: {self.cantidad}")

    def actualizar_precio(self, nuevo_precio):
        self.precio = nuevo_precio

    def to_dict(self):
        return {
            "id_prenda": self.id_prenda,
            "nombre": self.nombre,
            "tipo": self.tipo,
            "color": self.color,
            "talla": self.talla,
            "precio": self.precio,
            "cantidad": self.cantidad
        }

    @staticmethod
    def from_dict(datos):
        return Prenda(
            datos["id_prenda"],
            datos["nombre"],
            datos["tipo"],
            datos["color"],
            datos["talla"],
            datos["precio"],
            datos["cantidad"]
        )
