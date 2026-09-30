from prenda import Prenda
from stock import Stock
from movimiento_stock import EntradaStock, SalidaStock, DevolucionStock, AjusteStock
from usuario import Usuario, Cliente, Administrador
from carrito import Carrito
from compra import Compra
from pago import PagoEfectivo, PagoTransferencia, PagoTarjeta, PagoPSE
from repositorio_json import RepositorioJSON
from validaciones import pedir_texto, pedir_entero, pedir_float, pedir_opcion, validar_correo, validar_documento, validar_password
from datos_iniciales import cargar_prendas_iniciales, cargar_admin_inicial


class StyleMindApp:

    def __init__(self):
        self.repo = RepositorioJSON()
        self.stock = Stock()
        self.stock.cargar_stock()
        self.usuario_actual = None
        cargar_prendas_iniciales(self.stock)
        cargar_admin_inicial(self.repo)

    def ejecutar(self):
        print("==========================================")
        print("   Bienvenido a StyleMind!")
        print("   La tienda con las prendas mas cool")
        print("==========================================")

        while True:
            print("\nMenu principal:")
            print(" 1. Iniciar sesion")
            print(" 2. Registrarse")
            print(" 3. Recuperar contrasena")
            print(" 4. Salir")

            opcion = pedir_opcion("Ingresa una opcion: ", ["1", "2", "3", "4"])

            if opcion == "1":
                self.login()
            elif opcion == "2":
                self.registrar()
            elif opcion == "3":
                self.restablecer_contrasena()
            elif opcion == "4":
                print("Hasta pronto!")
                break

    def login(self):
        print("\n--- Iniciar sesion ---")
        documento = pedir_texto("Documento: ")
        password = pedir_texto("Contrasena: ")

        usuarios = self.repo.leer("usuarios.json")
        for u in usuarios:
            if u["documento"] == documento and u["password"] == password:
                self.usuario_actual = Usuario.from_dict(u)
                print(f"\nBienvenido {self.usuario_actual.nombre}!")

                if self.usuario_actual.rol == "admin":
                    self.menu_administrador()
                else:
                    self.menu_cliente()
                return

        print("Documento o contrasena incorrectos.")

    def registrar(self):
        print("\n--- Registro de cliente ---")
        nombre = pedir_texto("Nombre completo: ")

        while True:
            documento = pedir_texto("Documento: ")
            if not validar_documento(documento):
                print("El documento debe tener al menos 5 digitos.")
                continue
            usuarios = self.repo.leer("usuarios.json")
            existe = False
            for u in usuarios:
                if u["documento"] == documento:
                    existe = True
                    break
            if existe:
                print("Ya existe un usuario con ese documento.")
                continue
            break

        while True:
            correo = pedir_texto("Correo: ")
            if not validar_correo(correo):
                print("Ingresa un correo valido.")
                continue
            usuarios = self.repo.leer("usuarios.json")
            existe = False
            for u in usuarios:
                if u["correo"] == correo:
                    existe = True
                    break
            if existe:
                print("Ya existe un usuario con ese correo.")
                continue
            break

        while True:
            password = pedir_texto("Contrasena (minimo 4 caracteres): ")
            if validar_password(password):
                break
            print("La contrasena debe tener al menos 4 caracteres.")

        usuarios = self.repo.leer("usuarios.json")
        nuevo_id = len(usuarios) + 1
        cliente = Cliente(nuevo_id, nombre, documento, correo, password)
        self.repo.agregar_registro("usuarios.json", cliente.to_dict())
        print(f"Registro exitoso! Bienvenido {nombre}.")

    def restablecer_contrasena(self):
        print("\n--- Recuperar contrasena ---")
        dato = pedir_texto("Ingresa tu documento o correo: ")

        usuarios = self.repo.leer("usuarios.json")
        for i, u in enumerate(usuarios):
            if u["documento"] == dato or u["correo"] == dato:
                print(f"Usuario encontrado: {u['nombre']}")
                while True:
                    nueva = pedir_texto("Nueva contrasena (minimo 4 caracteres): ")
                    if validar_password(nueva):
                        break
                    print("La contrasena debe tener al menos 4 caracteres.")
                usuarios[i]["password"] = nueva
                self.repo.actualizar_registros("usuarios.json", usuarios)
                print("Contrasena actualizada exitosamente.")
                return

        print("No se encontro un usuario con ese dato.")

    def menu_cliente(self):
        while True:
            print(f"\nMenu cliente - {self.usuario_actual.nombre}:")
            print(" 1. Ver productos")
            print(" 2. Agregar al carrito")
            print(" 3. Ver carrito")
            print(" 4. Eliminar del carrito")
            print(" 5. Confirmar compra")
            print(" 6. Mi historial de compras")
            print(" 7. Cerrar sesion")

            opcion = pedir_opcion("Ingresa una opcion: ", ["1", "2", "3", "4", "5", "6", "7"])

            if opcion == "1":
                print("\nProductos disponibles:")
                self.stock.listar_disponibles()

            elif opcion == "2":
                self.agregar_al_carrito()

            elif opcion == "3":
                print("\nTu carrito:")
                self.usuario_actual.carrito.mostrar_carrito()

            elif opcion == "4":
                self.eliminar_del_carrito()

            elif opcion == "5":
                self.confirmar_compra()

            elif opcion == "6":
                self.ver_historial_cliente()

            elif opcion == "7":
                self.usuario_actual = None
                print("Sesion cerrada.")
                break

    def agregar_al_carrito(self):
        print("\nProductos disponibles:")
        self.stock.listar_disponibles()
        id_prenda = pedir_entero("ID de la prenda que deseas: ")
        prenda = self.stock.buscar_prenda(id_prenda)

        if prenda is None:
            print("Prenda no encontrada.")
            return

        cantidad = pedir_entero("Cantidad: ")

        if not self.stock.verificar_disponibilidad(id_prenda, cantidad):
            print(f"Stock insuficiente. Solo hay {prenda.cantidad} unidades.")
            return

        self.usuario_actual.carrito.agregar_producto(prenda, cantidad)

    def eliminar_del_carrito(self):
        if self.usuario_actual.carrito.esta_vacio():
            print("  El carrito esta vacio.")
            return
        print("\nTu carrito:")
        self.usuario_actual.carrito.mostrar_carrito()
        id_prenda = pedir_entero("ID de la prenda a eliminar: ")
        self.usuario_actual.carrito.eliminar_producto(id_prenda)

    def confirmar_compra(self):
        if self.usuario_actual.carrito.esta_vacio():
            print("  El carrito esta vacio. Agrega productos antes de comprar.")
            return

        print("\nResumen de tu carrito:")
        self.usuario_actual.carrito.mostrar_carrito()

        for item in self.usuario_actual.carrito.obtener_items():
            if not self.stock.verificar_disponibilidad(item["id_prenda"], item["cantidad"]):
                prenda = self.stock.buscar_prenda(item["id_prenda"])
                stock_actual = prenda.cantidad if prenda else 0
                print(f"  Stock insuficiente para {item['nombre']}. Disponible: {stock_actual}")
                return

        confirmacion = pedir_opcion("Confirmas la compra? (1. Si / 2. No): ", ["1", "2"])
        if confirmacion == "2":
            print("  Compra cancelada.")
            return

        metodo_pago = self.seleccionar_metodo_pago()
        if metodo_pago is None:
            return

        total = self.usuario_actual.carrito.calcular_total()
        metodo_pago.procesar_pago(total)

        compras = self.repo.leer("compras.json")
        id_compra = len(compras) + 1

        items_compra = self.usuario_actual.carrito.obtener_items()

        compra = Compra(
            id_compra,
            self.usuario_actual.documento,
            items_compra,
            total,
            metodo_pago.tipo
        )

        movimientos = self.repo.leer("movimientos.json")
        id_mov = len(movimientos) + 1

        for item in items_compra:
            salida = SalidaStock(id_mov, item["id_prenda"], item["cantidad"])
            salida.aplicar(self.stock)
            self.repo.agregar_registro("movimientos.json", salida.to_dict())
            id_mov += 1

        self.repo.agregar_registro("compras.json", compra.to_dict())

        pagos = self.repo.leer("pagos.json")
        id_pago = len(pagos) + 1
        pago_dict = metodo_pago.to_dict(id_pago, id_compra, total)
        self.repo.agregar_registro("pagos.json", pago_dict)

        compra.generar_resumen()
        self.usuario_actual.carrito.vaciar()

    def seleccionar_metodo_pago(self):
        print("\nMetodos de pago:")
        print(" 1. Efectivo")
        print(" 2. Transferencia")
        print(" 3. Tarjeta")
        print(" 4. PSE")

        opcion = pedir_opcion("Selecciona un metodo: ", ["1", "2", "3", "4"])

        if opcion == "1":
            return PagoEfectivo()
        elif opcion == "2":
            return PagoTransferencia()
        elif opcion == "3":
            return PagoTarjeta()
        elif opcion == "4":
            return PagoPSE()

    def ver_historial_cliente(self):
        compras = self.repo.leer("compras.json")
        mis_compras = []
        for c in compras:
            if c["documento_usuario"] == self.usuario_actual.documento:
                mis_compras.append(c)

        if len(mis_compras) == 0:
            print("  No tienes compras registradas.")
            return

        print(f"\nHistorial de compras de {self.usuario_actual.nombre}:")
        for c in mis_compras:
            compra = Compra.from_dict(c)
            compra.generar_resumen()

    def menu_administrador(self):
        while True:
            print(f"\nMenu administrador - {self.usuario_actual.nombre}:")
            print(" 1. Ver inventario")
            print(" 2. Agregar nueva prenda")
            print(" 3. Entrada de mercancia")
            print(" 4. Devolucion de producto")
            print(" 5. Ajuste de inventario")
            print(" 6. Ver movimientos de stock")
            print(" 7. Ver historial de compras")
            print(" 8. Cerrar sesion")

            opcion = pedir_opcion("Ingresa una opcion: ", ["1", "2", "3", "4", "5", "6", "7", "8"])

            if opcion == "1":
                print("\nInventario completo:")
                self.stock.listar_prendas()

            elif opcion == "2":
                self.admin_agregar_prenda()

            elif opcion == "3":
                self.admin_entrada_stock()

            elif opcion == "4":
                self.admin_devolucion()

            elif opcion == "5":
                self.admin_ajuste()

            elif opcion == "6":
                self.ver_movimientos()

            elif opcion == "7":
                self.ver_historial_general()

            elif opcion == "8":
                self.usuario_actual = None
                print("Sesion cerrada.")
                break

    def admin_agregar_prenda(self):
        print("\n--- Agregar nueva prenda ---")
        nombre = pedir_texto("Nombre de la prenda: ")

        print("Tipos: Camisa, Pantalon, Chaqueta")
        tipo = pedir_texto("Tipo: ")

        print("Colores: Negro, Beige, Blanco, Azul, Verde bosque")
        color = pedir_texto("Color: ")

        print("Tallas: S, M, L, XL")
        talla = pedir_texto("Talla: ")

        precio = pedir_float("Precio: ")
        cantidad = pedir_entero("Cantidad inicial: ")

        nuevo_id = self.stock.generar_id()
        prenda = Prenda(nuevo_id, nombre, tipo, color, talla, precio, cantidad)
        self.stock.agregar_prenda(prenda)

        movimientos = self.repo.leer("movimientos.json")
        id_mov = len(movimientos) + 1
        entrada = EntradaStock(id_mov, nuevo_id, cantidad)
        self.repo.agregar_registro("movimientos.json", entrada.to_dict())

        print(f"  Prenda agregada con ID [{nuevo_id}].")
        prenda.mostrar_info()

    def admin_entrada_stock(self):
        print("\n--- Entrada de mercancia ---")
        self.stock.listar_prendas()
        id_prenda = pedir_entero("ID de la prenda: ")
        prenda = self.stock.buscar_prenda(id_prenda)

        if prenda is None:
            print("  Prenda no encontrada.")
            return

        cantidad = pedir_entero("Cantidad a ingresar: ")

        movimientos = self.repo.leer("movimientos.json")
        id_mov = len(movimientos) + 1
        entrada = EntradaStock(id_mov, id_prenda, cantidad)
        resultado = entrada.aplicar(self.stock)

        if resultado:
            self.repo.agregar_registro("movimientos.json", entrada.to_dict())

    def admin_devolucion(self):
        print("\n--- Devolucion de producto ---")
        self.stock.listar_prendas()
        id_prenda = pedir_entero("ID de la prenda a devolver: ")
        prenda = self.stock.buscar_prenda(id_prenda)

        if prenda is None:
            print("  Prenda no encontrada.")
            return

        cantidad = pedir_entero("Cantidad devuelta: ")

        movimientos = self.repo.leer("movimientos.json")
        id_mov = len(movimientos) + 1
        devolucion = DevolucionStock(id_mov, id_prenda, cantidad)
        resultado = devolucion.aplicar(self.stock)

        if resultado:
            self.repo.agregar_registro("movimientos.json", devolucion.to_dict())

    def admin_ajuste(self):
        print("\n--- Ajuste de inventario ---")
        self.stock.listar_prendas()
        id_prenda = pedir_entero("ID de la prenda: ")
        prenda = self.stock.buscar_prenda(id_prenda)

        if prenda is None:
            print("  Prenda no encontrada.")
            return

        print(f"  Stock actual de {prenda.nombre}: {prenda.cantidad}")
        cantidad = pedir_entero("Nueva cantidad: ")

        movimientos = self.repo.leer("movimientos.json")
        id_mov = len(movimientos) + 1
        ajuste = AjusteStock(id_mov, id_prenda, cantidad)
        resultado = ajuste.aplicar(self.stock)

        if resultado:
            self.repo.agregar_registro("movimientos.json", ajuste.to_dict())

    def ver_movimientos(self):
        movimientos = self.repo.leer("movimientos.json")
        if len(movimientos) == 0:
            print("  No hay movimientos registrados.")
            return

        print("\nMovimientos de inventario:")
        for m in movimientos:
            print(f"  [{m['id_movimiento']}] {m['tipo'].upper()} | Prenda [{m['id_prenda']}] | Cant: {m['cantidad']} | {m['fecha']}")

    def ver_historial_general(self):
        compras = self.repo.leer("compras.json")
        if len(compras) == 0:
            print("  No hay compras registradas.")
            return

        print("\nHistorial general de compras:")
        for c in compras:
            compra = Compra.from_dict(c)
            compra.generar_resumen()
