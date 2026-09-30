from datetime import datetime


class MetodoPago:

    def __init__(self, tipo):
        self.tipo = tipo

    def procesar_pago(self, total):
        pass

    def to_dict(self, id_pago, id_compra, total):
        return {
            "id_pago": id_pago,
            "id_compra": id_compra,
            "tipo": self.tipo,
            "total": total,
            "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }


class PagoEfectivo(MetodoPago):

    def __init__(self):
        super().__init__("efectivo")

    def procesar_pago(self, total):
        print(f"  Pago en efectivo procesado por ${total:,.0f}")
        return True


class PagoTransferencia(MetodoPago):

    def __init__(self):
        super().__init__("transferencia")

    def procesar_pago(self, total):
        print(f"  Pago por transferencia procesado por ${total:,.0f}")
        print("  Referencia: TRF-" + datetime.now().strftime("%Y%m%d%H%M%S"))
        return True


class PagoTarjeta(MetodoPago):

    def __init__(self):
        super().__init__("tarjeta")

    def procesar_pago(self, total):
        print(f"  Pago con tarjeta procesado por ${total:,.0f}")
        print("  Ultimos 4 digitos: ****")
        return True


class PagoPSE(MetodoPago):

    def __init__(self):
        super().__init__("PSE")

    def procesar_pago(self, total):
        print(f"  Pago por PSE procesado por ${total:,.0f}")
        print("  Redirigiendo a entidad bancaria...")
        return True
