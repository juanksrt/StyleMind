from prenda import Prenda
from usuario import Administrador


def cargar_prendas_iniciales(stock):
    if len(stock.prendas) > 0:
        return

    prendas = [
        Prenda(1, "Camisa Clasica", "Camisa", "Negro", "S", 45000, 20),
        Prenda(2, "Camisa Clasica", "Camisa", "Negro", "M", 50000, 20),
        Prenda(3, "Camisa Clasica", "Camisa", "Negro", "L", 55000, 8),
        Prenda(4, "Camisa Clasica", "Camisa", "Negro", "XL", 62000, 8),
        Prenda(5, "Camisa Clasica", "Camisa", "Beige", "S", 45000, 20),
        Prenda(6, "Camisa Clasica", "Camisa", "Beige", "M", 50000, 20),
        Prenda(7, "Camisa Clasica", "Camisa", "Beige", "L", 55000, 8),
        Prenda(8, "Camisa Clasica", "Camisa", "Beige", "XL", 62000, 8),
        Prenda(9, "Camisa Clasica", "Camisa", "Blanco", "S", 45000, 20),
        Prenda(10, "Camisa Clasica", "Camisa", "Blanco", "M", 50000, 20),
        Prenda(11, "Camisa Clasica", "Camisa", "Blanco", "L", 55000, 8),
        Prenda(12, "Camisa Clasica", "Camisa", "Blanco", "XL", 62000, 8),
        Prenda(13, "Camisa Urban", "Camisa", "Azul", "S", 45000, 8),
        Prenda(14, "Camisa Urban", "Camisa", "Azul", "M", 50000, 8),
        Prenda(15, "Camisa Urban", "Camisa", "Azul", "L", 55000, 5),
        Prenda(16, "Camisa Urban", "Camisa", "Azul", "XL", 62000, 5),
        Prenda(17, "Camisa Urban", "Camisa", "Verde bosque", "S", 45000, 8),
        Prenda(18, "Camisa Urban", "Camisa", "Verde bosque", "M", 50000, 8),
        Prenda(19, "Camisa Urban", "Camisa", "Verde bosque", "L", 55000, 5),
        Prenda(20, "Camisa Urban", "Camisa", "Verde bosque", "XL", 62000, 5),
        Prenda(21, "Pantalon Slim", "Pantalon", "Negro", "S", 75000, 8),
        Prenda(22, "Pantalon Slim", "Pantalon", "Negro", "M", 82000, 8),
        Prenda(23, "Pantalon Slim", "Pantalon", "Negro", "L", 90000, 4),
        Prenda(24, "Pantalon Slim", "Pantalon", "Negro", "XL", 98000, 4),
        Prenda(25, "Pantalon Slim", "Pantalon", "Beige", "S", 75000, 8),
        Prenda(26, "Pantalon Slim", "Pantalon", "Beige", "M", 82000, 8),
        Prenda(27, "Pantalon Slim", "Pantalon", "Beige", "L", 90000, 4),
        Prenda(28, "Pantalon Slim", "Pantalon", "Beige", "XL", 98000, 4),
        Prenda(29, "Pantalon Slim", "Pantalon", "Blanco", "S", 75000, 8),
        Prenda(30, "Pantalon Slim", "Pantalon", "Blanco", "M", 82000, 8),
        Prenda(31, "Pantalon Slim", "Pantalon", "Blanco", "L", 90000, 4),
        Prenda(32, "Pantalon Slim", "Pantalon", "Blanco", "XL", 98000, 4),
        Prenda(33, "Pantalon Urban", "Pantalon", "Azul", "S", 75000, 6),
        Prenda(34, "Pantalon Urban", "Pantalon", "Azul", "M", 82000, 6),
        Prenda(35, "Pantalon Urban", "Pantalon", "Azul", "L", 90000, 2),
        Prenda(36, "Pantalon Urban", "Pantalon", "Azul", "XL", 98000, 2),
        Prenda(37, "Pantalon Urban", "Pantalon", "Verde bosque", "S", 75000, 6),
        Prenda(38, "Pantalon Urban", "Pantalon", "Verde bosque", "M", 82000, 6),
        Prenda(39, "Pantalon Urban", "Pantalon", "Verde bosque", "L", 90000, 2),
        Prenda(40, "Pantalon Urban", "Pantalon", "Verde bosque", "XL", 98000, 2),
        Prenda(41, "Chaqueta Premium", "Chaqueta", "Negro", "S", 89000, 10),
        Prenda(42, "Chaqueta Premium", "Chaqueta", "Negro", "M", 95000, 10),
        Prenda(43, "Chaqueta Premium", "Chaqueta", "Negro", "L", 102000, 5),
        Prenda(44, "Chaqueta Premium", "Chaqueta", "Negro", "XL", 110000, 5),
        Prenda(45, "Chaqueta Premium", "Chaqueta", "Beige", "S", 89000, 10),
        Prenda(46, "Chaqueta Premium", "Chaqueta", "Beige", "M", 95000, 10),
        Prenda(47, "Chaqueta Premium", "Chaqueta", "Beige", "L", 102000, 5),
        Prenda(48, "Chaqueta Premium", "Chaqueta", "Beige", "XL", 110000, 5),
        Prenda(49, "Chaqueta Premium", "Chaqueta", "Blanco", "S", 89000, 10),
        Prenda(50, "Chaqueta Premium", "Chaqueta", "Blanco", "M", 95000, 10),
        Prenda(51, "Chaqueta Premium", "Chaqueta", "Blanco", "L", 102000, 5),
        Prenda(52, "Chaqueta Premium", "Chaqueta", "Blanco", "XL", 110000, 5),
        Prenda(53, "Chaqueta Urban", "Chaqueta", "Azul", "S", 89000, 5),
        Prenda(54, "Chaqueta Urban", "Chaqueta", "Azul", "M", 95000, 5),
        Prenda(55, "Chaqueta Urban", "Chaqueta", "Azul", "L", 102000, 3),
        Prenda(56, "Chaqueta Urban", "Chaqueta", "Azul", "XL", 110000, 3),
        Prenda(57, "Chaqueta Urban", "Chaqueta", "Verde bosque", "S", 89000, 5),
        Prenda(58, "Chaqueta Urban", "Chaqueta", "Verde bosque", "M", 95000, 5),
        Prenda(59, "Chaqueta Urban", "Chaqueta", "Verde bosque", "L", 102000, 3),
        Prenda(60, "Chaqueta Urban", "Chaqueta", "Verde bosque", "XL", 110000, 3),
    ]

    for prenda in prendas:
        stock.prendas.append(prenda)

    stock.guardar_stock()
    print("  Inventario inicial cargado con 60 prendas.")


def cargar_admin_inicial(repo):
    usuarios = repo.leer("usuarios.json")
    for u in usuarios:
        if u["rol"] == "admin":
            return
    admin = Administrador(1, "Admin StyleMind", "0000000000", "admin@stylemind.com", "admin123")
    repo.agregar_registro("usuarios.json", admin.to_dict())
    print("  Administrador creado. Doc: 0000000000 | Pass: admin123")
