# ejemplo5_escuela.py
# Ejemplo del mundo real: Sistema Escolar usando Programación Orientada a Objetos (POO)

# Clase que representa un estudiante
class Estudiante:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.cursos = []

    def inscribirse(self, curso):
        self.cursos.append(curso)
        curso.agregar_estudiante(self)
        print(f"{self.nombre} se ha inscrito en el curso {curso.nombre}.")

    def mostrar_cursos(self):
        if not self.cursos:
            print(f"{self.nombre} no está inscrito en ningún curso.")
        else:
            print(f"Cursos de {self.nombre}:")
            for curso in self.cursos:
                print(f"- {curso.nombre}")


# Clase que representa un curso
class Curso:
    def __init__(self, nombre, profesor=None):
        self.nombre = nombre
        self.profesor = profesor
        self.estudiantes = []

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

    def asignar_profesor(self, profesor):
        self.profesor = profesor
        print(f"El profesor {profesor.nombre} ha sido asignado al curso {self.nombre}.")

    def mostrar_estudiantes(self):
        print(f"Estudiantes en el curso {self.nombre}:")
        if not self.estudiantes:
            print("No hay estudiantes inscritos.")
        else:
            for estudiante in self.estudiantes:
                print(f"- {estudiante.nombre}")


# Clase que representa un profesor
class Profesor:
    def __init__(self, nombre, especialidad):
        self.nombre = nombre
        self.especialidad = especialidad
        self.cursos = []

    def asignar_curso(self, curso):
        self.cursos.append(curso)
        curso.asignar_profesor(self)

    def mostrar_cursos(self):
        if not self.cursos:
            print(f"{self.nombre} no tiene cursos asignados.")
        else:
            print(f"Cursos asignados a {self.nombre}:")
            for curso in self.cursos:
                print(f"- {curso.nombre}")


# Ejemplo de uso
if __name__ == "__main__":
    # Crear profesor
    profesor1 = Profesor("Laura Gómez", "Matemáticas")

    # Crear cursos
    curso_mate = Curso("Matemáticas")
    curso_historia = Curso("Historia")

    # Asignar profesor a un curso
    profesor1.asignar_curso(curso_mate)

    # Crear estudiantes
    estudiante1 = Estudiante("Mercy", 21)
    estudiante2 = Estudiante("Carlos", 20)

    # Inscribir estudiantes en cursos
    estudiante1.inscribirse(curso_mate)
    estudiante2.inscribirse(curso_mate)
    estudiante1.inscribirse(curso_historia)

    # Mostrar la información
    curso_mate.mostrar_estudiantes()
    profesor1.mostrar_cursos()
    estudiante1.mostrar_cursos()
