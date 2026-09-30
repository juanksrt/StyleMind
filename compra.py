from datetime import datetime


class Compra:

    def __init__(self, id_compra, documento_usuario, productos, total, metodo_pago):
        self.id_compra = id_compra
        self.documento_usuario = documento_usuario
        self.productos = productos
        self.total = total
        self.metodo_pago = metodo_pago
        self.fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def generar_resumen(self):
        print("  ==========================================")
        print("           RESUMEN DE COMPRA")
        print("  ==========================================")
        print(f"  Compra #: {self.id_compra}")
        print(f"  Fecha: {self.fecha}")
        print(f"  Cliente: {self.documento_usuario}")
        print("  Productos:")
        i = 1
        for p in self.productos:
            subtotal = p["precio"] * p["cantidad"]
            print(f"    {i}. {p['nombre']} | {p['color']} | {p['talla']} | x{p['cantidad']} | ${subtotal:,.0f}")
            i += 1
        print(f"  Total: ${self.total:,.0f}")
        print(f"  Metodo de pago: {self.metodo_pago}")
        print("  ==========================================")

    def to_dict(self):
        return {
            "id_compra": self.id_compra,
            "documento_usuario": self.documento_usuario,
            "productos": self.productos,
            "total": self.total,
            "metodo_pago": self.metodo_pago,
            "fecha": self.fecha
        }

    @staticmethod
    def from_dict(datos):
        compra = Compra(
            datos["id_compra"],
            datos["documento_usuario"],
            datos["productos"],
            datos["total"],
            datos["metodo_pago"]
        )
        compra.fecha = datos["fecha"]
        return compra
