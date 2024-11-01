from persona import Persona

class Docente(Persona):
    def __init__(self, nombre, edad, asignatura, antiguedad):
        super().__init__(nombre, edad)
        self.asignatura = asignatura
        self.antiguedad = antiguedad

    def mostrar_info(self):
        return f"Docente: {self.nombre}, Edad: {self.edad}, Asignatura: {self.asignatura}, Antigüedad: {self.antiguedad} años"
