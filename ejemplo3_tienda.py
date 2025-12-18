# ejemplo3_tienda.py
# Ejemplo del mundo real con POO: Tienda y Productos

# Clase que representa un producto
class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def mostrar_informacion(self):
        print(f"Producto: {self.nombre} | Precio: ${self.precio} | Stock: {self.stock} unidades")

    def vender(self, cantidad):
        if cantidad <= self.stock:
            self.stock -= cantidad
            print(f"Se vendieron {cantidad} unidades de {self.nombre}. Quedan {self.stock}.")
        else:
            print(f"No hay suficiente stock de {self.nombre} para vender {cantidad} unidades.")

# Clase que representa la tienda
class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []  # Lista para guardar objetos de tipo Producto

    def agregar_producto(self, producto):
        self.productos.append(producto)
        print(f"Se agregó {producto.nombre} a la tienda {self.nombre}.")

    def mostrar_productos(self):
        print(f"\nInventario de la tienda {self.nombre}:")
        for producto in self.productos:
            producto.mostrar_informacion()

# -----------------------------
# Programa principal
# -----------------------------

# Crear productos
p1 = Producto("Camiseta", 20, 15)
p2 = Producto("Pantalón", 35, 10)
p3 = Producto("Zapatos", 50, 5)

# Crear tienda
tienda1 = Tienda("Moda Center")

# Agregar productos a la tienda
tienda1.agregar_producto(p1)
tienda1.agregar_producto(p2)
tienda1.agregar_producto(p3)

# Mostrar inventario
tienda1.mostrar_productos()

# Realizar una venta
p1.vender(3)
p3.vender(1)

# Mostrar inventario actualizado
tienda1.mostrar_productos()
