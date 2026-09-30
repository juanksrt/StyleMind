from prenda import Prenda
from repositorio_json import RepositorioJSON


class Stock:

    def __init__(self):
        self.prendas = []
        self.repo = RepositorioJSON()

    def agregar_prenda(self, prenda):
        self.prendas.append(prenda)
        self.guardar_stock()

    def buscar_prenda(self, id_prenda):
        for prenda in self.prendas:
            if prenda.id_prenda == id_prenda:
                return prenda
        return None

    def listar_prendas(self):
        if len(self.prendas) == 0:
            print("  No hay prendas en el inventario.")
            return
        for prenda in self.prendas:
            prenda.mostrar_info()

    def listar_disponibles(self):
        disponibles = []
        for prenda in self.prendas:
            if prenda.cantidad > 0:
                disponibles.append(prenda)
        if len(disponibles) == 0:
            print("  No hay prendas disponibles.")
            return
        for prenda in disponibles:
            prenda.mostrar_info()

    def verificar_disponibilidad(self, id_prenda, cantidad):
        prenda = self.buscar_prenda(id_prenda)
        if prenda is None:
            return False
        return prenda.cantidad >= cantidad

    def entrada_stock(self, id_prenda, cantidad):
        prenda = self.buscar_prenda(id_prenda)
        if prenda is not None:
            prenda.cantidad += cantidad
            self.guardar_stock()
            return True
        return False

    def salida_stock(self, id_prenda, cantidad):
        prenda = self.buscar_prenda(id_prenda)
        if prenda is not None and prenda.cantidad >= cantidad:
            prenda.cantidad -= cantidad
            self.guardar_stock()
            return True
        return False

    def devolucion_stock(self, id_prenda, cantidad):
        prenda = self.buscar_prenda(id_prenda)
        if prenda is not None:
            prenda.cantidad += cantidad
            self.guardar_stock()
            return True
        return False

    def ajuste_stock(self, id_prenda, nueva_cantidad):
        prenda = self.buscar_prenda(id_prenda)
        if prenda is not None:
            prenda.cantidad = nueva_cantidad
            self.guardar_stock()
            return True
        return False

    def generar_id(self):
        if len(self.prendas) == 0:
            return 1
        ids = []
        for p in self.prendas:
            ids.append(p.id_prenda)
        return max(ids) + 1

    def guardar_stock(self):
        datos = []
        for prenda in self.prendas:
            datos.append(prenda.to_dict())
        self.repo.escribir("prendas.json", datos)

    def cargar_stock(self):
        datos = self.repo.leer("prendas.json")
        self.prendas = []
        for d in datos:
            self.prendas.append(Prenda.from_dict(d))
