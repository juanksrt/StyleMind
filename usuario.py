from carrito import Carrito


class Usuario:

    def __init__(self, id_usuario, nombre, documento, correo, password, rol):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.documento = documento
        self.correo = correo
        self.password = password
        self.rol = rol

    def mostrar_info(self):
        print(f"  {self.nombre} | Doc: {self.documento} | {self.correo} | Rol: {self.rol}")

    def to_dict(self):
        return {
            "id_usuario": self.id_usuario,
            "nombre": self.nombre,
            "documento": self.documento,
            "correo": self.correo,
            "password": self.password,
            "rol": self.rol
        }

    @staticmethod
    def from_dict(datos):
        if datos["rol"] == "admin":
            return Administrador(
                datos["id_usuario"],
                datos["nombre"],
                datos["documento"],
                datos["correo"],
                datos["password"]
            )
        else:
            return Cliente(
                datos["id_usuario"],
                datos["nombre"],
                datos["documento"],
                datos["correo"],
                datos["password"]
            )


class Cliente(Usuario):

    def __init__(self, id_usuario, nombre, documento, correo, password):
        super().__init__(id_usuario, nombre, documento, correo, password, "cliente")
        self.carrito = Carrito()


class Administrador(Usuario):

    def __init__(self, id_usuario, nombre, documento, correo, password):
        super().__init__(id_usuario, nombre, documento, correo, password, "admin")
