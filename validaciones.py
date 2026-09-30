def pedir_texto(mensaje):
    while True:
        valor = input(mensaje).strip()
        if valor != "":
            return valor
        print("Este campo no puede estar vacio.")


def pedir_entero(mensaje):
    while True:
        valor = input(mensaje).strip()
        if valor.isdigit() and int(valor) > 0:
            return int(valor)
        print("Ingresa un numero entero positivo.")


def pedir_float(mensaje):
    while True:
        valor = input(mensaje).strip()
        try:
            numero = float(valor)
            if numero > 0:
                return numero
            print("El valor debe ser mayor a 0.")
        except ValueError:
            print("Ingresa un numero valido.")


def pedir_opcion(mensaje, opciones_validas):
    while True:
        valor = input(mensaje).strip()
        if valor in opciones_validas:
            return valor
        print(f"Opcion no valida. Opciones: {', '.join(opciones_validas)}")


def validar_correo(correo):
    return "@" in correo and "." in correo


def validar_documento(documento):
    return documento.isdigit() and len(documento) >= 5


def validar_password(password):
    return len(password) >= 4
