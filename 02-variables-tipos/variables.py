"""
Una variable es un contenedor de información. En Python, no es necesario declarar el tipo de variable,
ya que el propio lenguaje lo infiere en función del valor asignado.
Existen varios tipos de variables en Python, entre los más comunes se encuentran:
- int: para números enteros.
- float: para números decimales.
- str: para cadenas de texto.
- bool: para valores booleanos (True o False).
"""

texto = "Master en python!"  # str
print(texto)

#python es un lenguaje de tipado dinámico, lo que significa que no es necesario declarar el tipo de variable.
#El tipo de variable se infiere automáticamente en función del valor asignado.

entero = 42          # int
decimal = 3.14      # float
booleano = True     # bool
print(entero)
print(decimal)  
print(booleano)

print("----------------------------")

# Podemos cambiar el valor y el tipo de una variable en cualquier momento.
entero = "Ahora soy una cadena"  # str
print(entero)

print("----------------------------")

#conncatencación de cadenas

nombre = "Juan"
apellido = "Pérez"
nombre_completo = nombre + " " + apellido
print(nombre_completo)
edad = 30
mensaje = nombre + " tiene " + str(edad) + " años."
print(mensaje)

    
#Otra forma de concatenar cadenas es usando f-strings (disponible en Python 3.6+)
mensaje_fstring = f"{nombre} tiene {edad} años."
print(mensaje_fstring)

# También podemos usar el método format()
mensaje_format = "{} tiene {} años.".format(nombre, edad)
print(mensaje_format)
