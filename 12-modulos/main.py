"""
Modulos en Python:
- Un módulo es un archivo que contiene código Python que puede ser reutilizado en otros programas.
- Los módulos permiten organizar el código en partes más pequeñas y manejables.
- Se pueden importar módulos utilizando la palabra clave 'import' seguida del nombre del módulo.
- Los módulos pueden contener funciones, clases y variables que pueden ser utilizadas en otros programas.
- Python viene con una biblioteca estándar que incluye muchos módulos útiles para diversas tareas.
- También es posible crear módulos personalizados para reutilizar código específico en diferentes proyectos.
- Para crear un módulo personalizado, simplemente crea un archivo .py con el código que deseas reutilizar.
- Pagina oficial: https://docs.python.org/3/py-modindex.html
"""
# Importar el módulo completo
import mimodulo

print(mimodulo.holaMundo("Cinlo Losada"))
print(mimodulo.calculadora(10, 5))
print(mimodulo.calculadora(10, 5, True))


# si quiero importar algo en concreto del modulo
from mimodulo import holaMundo

print(holaMundo("Cinlo Losada"))

# Modulo de fechas

import datetime
print(datetime.date.today())

fecha_completa = datetime.datetime.now()
print(fecha_completa)
print("Fecha:", fecha_completa.day)
print("Mes:", fecha_completa.month) 
print("Año:", fecha_completa.year)
print("Hora:", fecha_completa.hour)

fecha_personalizada = fecha_completa.strftime("%d/%m/%Y, %H:%M:%S")
print("Fecha personalizada:", fecha_personalizada)

# Modulo matematicas
import math
print("Número Pi:", math.pi)
print("Raíz cuadrada de 16:", math.sqrt(16))
print("Redondear 7.8 hacia arriba:", math.ceil(7.8))
print("Redondear 7.2 hacia abajo:", math.floor(7.2))
print("Seno de 90 grados:", math.sin(math.radians(90)))
print("Coseno de 0 grados:", math.cos(math.radians(0)))

