# ejemplo4_biblioteca.py
# Ejemplo del mundo real: Sistema de Biblioteca usando POO

# Clase que representa a un usuario de la biblioteca
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def tomar_prestado(self, libro):
        if libro.disponible:
            libro.disponible = False
            self.libros_prestados.append(libro)
            print(f"{self.nombre} ha tomado prestado el libro '{libro.titulo}'.")
        else:
            print(f"El libro '{libro.titulo}' no está disponible actualmente.")

    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            libro.disponible = True
            self.libros_prestados.remove(libro)
            print(f"{self.nombre} ha devuelto el libro '{libro.titulo}'.")
        else:
            print(f"{self.nombre} no tiene el libro '{libro.titulo}' prestado.")

    def mostrar_libros_prestados(self):
        if not self.libros_prestados:
            print(f"{self.nombre} no tiene libros prestados.")
        else:
            print(f"Libros prestados por {self.nombre}:")
            for libro in self.libros_prestados:
                print(f"- {libro.titulo} de {libro.autor}")


# Clase que representa un libro
class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponible = True


# Clase que representa un préstamo
class Prestamo:
    def __init__(self, usuario, libro):
        self.usuario = usuario
        self.libro = libro

    def realizar_prestamo(self):
        self.usuario.tomar_prestado(self.libro)

    def devolver_prestamo(self):
        self.usuario.devolver_libro(self.libro)


# Ejemplo de uso
if __name__ == "__main__":
    # Crear libros
    libro1 = Libro("Cien años de soledad", "Gabriel García Márquez")
    libro2 = Libro("El Principito", "Antoine de Saint-Exupéry")

    # Crear usuario
    usuario1 = Usuario("Mercy", 1)

    # Crear préstamos
    prestamo1 = Prestamo(usuario1, libro1)
    prestamo2 = Prestamo(usuario1, libro2)

    # Realizar préstamos
    prestamo1.realizar_prestamo()
    prestamo2.realizar_prestamo()

    # Mostrar libros prestados
    usuario1.mostrar_libros_prestados()

    # Devolver un libro
    prestamo1.devolver_prestamo()

    # Mostrar libros después de devolver uno
    usuario1.mostrar_libros_prestados()
