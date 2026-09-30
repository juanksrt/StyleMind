class Carrito:

    def __init__(self):
        self.items = []

    def agregar_producto(self, prenda, cantidad):
        for item in self.items:
            if item["id_prenda"] == prenda.id_prenda:
                item["cantidad"] += cantidad
                print(f"  Se actualizo la cantidad de {prenda.nombre} en el carrito.")
                return
        self.items.append({
            "id_prenda": prenda.id_prenda,
            "nombre": prenda.nombre,
            "tipo": prenda.tipo,
            "color": prenda.color,
            "talla": prenda.talla,
            "precio": prenda.precio,
            "cantidad": cantidad
        })
        print(f"  {prenda.nombre} agregado al carrito.")

    def eliminar_producto(self, id_prenda):
        for i, item in enumerate(self.items):
            if item["id_prenda"] == id_prenda:
                nombre = item["nombre"]
                self.items.pop(i)
                print(f"  {nombre} eliminado del carrito.")
                return True
        print("  Producto no encontrado en el carrito.")
        return False

    def modificar_cantidad(self, id_prenda, nueva_cantidad):
        for item in self.items:
            if item["id_prenda"] == id_prenda:
                item["cantidad"] = nueva_cantidad
                print(f"  Cantidad de {item['nombre']} actualizada a {nueva_cantidad}.")
                return True
        print("  Producto no encontrado en el carrito.")
        return False

    def calcular_total(self):
        total = 0
        for item in self.items:
            total += item["precio"] * item["cantidad"]
        return total

    def mostrar_carrito(self):
        if len(self.items) == 0:
            print("  El carrito esta vacio.")
            return
        print("  Productos en tu carrito:")
        i = 1
        for item in self.items:
            subtotal = item["precio"] * item["cantidad"]
            print(f"  {i}. {item['nombre']} | {item['color']} | {item['talla']} | x{item['cantidad']} | ${subtotal:,.0f}")
            i += 1
        print(f"  TOTAL: ${self.calcular_total():,.0f}")

    def vaciar(self):
        self.items = []

    def esta_vacio(self):
        return len(self.items) == 0

    def obtener_items(self):
        return list(self.items)
