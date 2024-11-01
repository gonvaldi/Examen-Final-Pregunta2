from estudiante import Estudiante
from administrativo import Administrativo
from docente import Docente


# Crear objetos de ejemplo
estudiante1 = Estudiante("Gabriel Garcia", 18, "55202301", "Literatura")
administrativo1 = Administrativo("Claudia Goldin", 35, "Administradora", "Administración")
docente1 = Docente("Hiroshi Amano", 60, "Física", 30)

# Mostrar información
print(estudiante1.mostrar_info())
print(administrativo1.mostrar_info())
print(docente1.mostrar_info())
