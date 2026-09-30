import json
import os


class RepositorioJSON:

    def __init__(self, carpeta="datos"):
        self.carpeta = carpeta
        if not os.path.exists(self.carpeta):
            os.makedirs(self.carpeta)

    def ruta(self, nombre_archivo):
        return os.path.join(self.carpeta, nombre_archivo)

    def crear_si_no_existe(self, nombre_archivo):
        archivo = self.ruta(nombre_archivo)
        if not os.path.exists(archivo):
            with open(archivo, "w", encoding="utf-8") as f:
                json.dump([], f)

    def leer(self, nombre_archivo):
        self.crear_si_no_existe(nombre_archivo)
        archivo = self.ruta(nombre_archivo)
        try:
            with open(archivo, "r", encoding="utf-8") as f:
                contenido = f.read().strip()
                if contenido == "":
                    return []
                return json.loads(contenido)
        except (json.JSONDecodeError, ValueError):
            return []

    def escribir(self, nombre_archivo, datos):
        archivo = self.ruta(nombre_archivo)
        with open(archivo, "w", encoding="utf-8") as f:
            json.dump(datos, f, indent=4, ensure_ascii=False)

    def agregar_registro(self, nombre_archivo, registro):
        datos = self.leer(nombre_archivo)
        datos.append(registro)
        self.escribir(nombre_archivo, datos)

    def actualizar_registros(self, nombre_archivo, datos):
        self.escribir(nombre_archivo, datos)
