nada = None
#imprimir variable
print(nada)  # None
#imprimir el tipo de la variable
print(type(nada))  # <class 'NoneType'>

print("----------------------------")

cadena = "Hola soy CinloDev"  
cadena = " y esto es Python."
print(cadena) 
print(type(cadena))  # <class 'str'>


print("----------------------------")

numero_entero = 100
print(numero_entero)
print(type(numero_entero))  # <class 'int'>

print("----------------------------")
numero_decimal = 12.34
print(numero_decimal)
print(type(numero_decimal))  # <class 'float'>

print("----------------------------")
booleano = False
print(booleano)
print(type(booleano))  # <class 'bool'>

print("----------------------------")

lista = [1, 2, 3, 4, 5]
print(lista)
print(type(lista))  # <class 'list'>

print("----------------------------")

tupla = (10, 20, 30)
print(tupla)
print(type(tupla))  # <class 'tuple'>

print("----------------------------")

conjunto = { 'manzana', 'banana', 'cereza' }
print(conjunto)
print(type(conjunto))  # <class 'set'>

print("----------------------------")

diccionario = { 'nombre': 'Ana', 'edad': 25 }
print(diccionario)
print(type(diccionario))  # <class 'dict'>

print("----------------------------")

rango = range(1, 10)
print(rango)
print(type(rango))  # <class 'range'>

print("----------------------------")
print("----------------------------")

#concatenacion de distintos tipos de datos
nombre = "Ana"
edad = 25
mensaje = nombre + " tiene " + str(edad) + " años."
print(mensaje)

#Otra forma de concatenar cadenas es usando f-strings (disponible en Python 3.6+)
mensaje_fstring = f"{nombre} tiene {edad} años."
print(mensaje_fstring)
# También podemos usar el método format()
mensaje_format = "{} tiene {} años.".format(nombre, edad)
print(mensaje_format)

texto = "Master en python!"  # str
numerito = 42          # int
print(texto)
print(type(texto))
print(numerito)
print(type(numerito))

numerito = str(numerito)  
print(numerito)
print(type(numerito))  # <class 'str'>

numerito = float(numerito)
print(numerito)
print(type(numerito))  # <class 'float'>

print("----------------------------")
print("----------------------------")
