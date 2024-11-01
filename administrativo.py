from persona import Persona

class Administrativo(Persona):
    def __init__(self, nombre, edad, cargo, area):
        super().__init__(nombre, edad)
        self.cargo = cargo
        self.area = area

    def mostrar_info(self):
        return f"Administrativo: {self.nombre}, Edad: {self.edad}, Cargo: {self.cargo}, Área: {self.area}"
