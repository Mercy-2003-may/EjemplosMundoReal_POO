# ejemplo2_vehiculo.py
# Ejemplo de Programación Orientada a Objetos (POO)
# Clase que representa un vehículo del mundo real

class Vehiculo:
    # Constructor (método que se ejecuta al crear un objeto)
    def __init__(self, marca, modelo, año):
        self.marca = marca      # Atributo de instancia
        self.modelo = modelo
        self.año = año
        self.encendido = False  # Estado inicial del vehículo

    # Método para encender el vehículo
    def encender(self):
        if not self.encendido:
            self.encendido = True
            print(f"El {self.marca} {self.modelo} ha sido encendido.")
        else:
            print("El vehículo ya está encendido.")

    # Método para apagar el vehículo
    def apagar(self):
        if self.encendido:
            self.encendido = False
            print(f"El {self.marca} {self.modelo} ha sido apagado.")
        else:
            print("El vehículo ya está apagado.")

    # Método para mostrar información del vehículo
    def mostrar_informacion(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.año}")

# -----------------------------
# Programa principal
# -----------------------------

auto1 = Vehiculo("Toyota", "Corolla", 2020)
auto2 = Vehiculo("Honda", "Civic", 2022)

auto1.mostrar_informacion()
auto1.encender()
auto1.apagar()

auto2.mostrar_informacion()
auto2.encender()
