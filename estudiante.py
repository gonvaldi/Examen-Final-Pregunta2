from persona import Persona

class Estudiante(Persona):
    def __init__(self, nombre, edad, matricula, carrera):
        super().__init__(nombre, edad)
        self.matricula = matricula
        self.carrera = carrera

    def mostrar_info(self):
        return f"Estudiante: {self.nombre}, Edad: {self.edad}, Matrícula: {self.matricula}, Carrera: {self.carrera}"
