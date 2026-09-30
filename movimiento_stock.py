from datetime import datetime
from repositorio_json import RepositorioJSON


class MovimientoStock:

    def __init__(self, id_movimiento, id_prenda, cantidad, tipo_movimiento):
        self.id_movimiento = id_movimiento
        self.id_prenda = id_prenda
        self.cantidad = cantidad
        self.tipo_movimiento = tipo_movimiento
        self.fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def aplicar(self, stock):
        pass

    def to_dict(self):
        return {
            "id_movimiento": self.id_movimiento,
            "id_prenda": self.id_prenda,
            "cantidad": self.cantidad,
            "tipo": self.tipo_movimiento,
            "fecha": self.fecha
        }


class EntradaStock(MovimientoStock):

    def __init__(self, id_movimiento, id_prenda, cantidad):
        super().__init__(id_movimiento, id_prenda, cantidad, "entrada")

    def aplicar(self, stock):
        resultado = stock.entrada_stock(self.id_prenda, self.cantidad)
        if resultado:
            print(f"  Entrada registrada: +{self.cantidad} unidades a prenda [{self.id_prenda}]")
        else:
            print("  No se pudo registrar la entrada.")
        return resultado


class SalidaStock(MovimientoStock):

    def __init__(self, id_movimiento, id_prenda, cantidad):
        super().__init__(id_movimiento, id_prenda, cantidad, "salida")

    def aplicar(self, stock):
        resultado = stock.salida_stock(self.id_prenda, self.cantidad)
        if resultado:
            print(f"  Salida registrada: -{self.cantidad} unidades de prenda [{self.id_prenda}]")
        else:
            print("  No se pudo registrar la salida. Stock insuficiente.")
        return resultado


class DevolucionStock(MovimientoStock):

    def __init__(self, id_movimiento, id_prenda, cantidad):
        super().__init__(id_movimiento, id_prenda, cantidad, "devolucion")

    def aplicar(self, stock):
        resultado = stock.devolucion_stock(self.id_prenda, self.cantidad)
        if resultado:
            print(f"  Devolucion registrada: +{self.cantidad} unidades a prenda [{self.id_prenda}]")
        else:
            print("  No se pudo registrar la devolucion.")
        return resultado


class AjusteStock(MovimientoStock):

    def __init__(self, id_movimiento, id_prenda, cantidad):
        super().__init__(id_movimiento, id_prenda, cantidad, "ajuste")

    def aplicar(self, stock):
        resultado = stock.ajuste_stock(self.id_prenda, self.cantidad)
        if resultado:
            print(f"  Ajuste registrado: prenda [{self.id_prenda}] ahora tiene {self.cantidad} unidades")
        else:
            print("  No se pudo registrar el ajuste.")
        return resultado
