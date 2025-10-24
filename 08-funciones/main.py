"""
FUNCIONES 
es un bloque de código reutilizable que realiza una tarea específica.

def nombre_de_la_funcion(parametros):
    # bloque de código
    return valor_de_retorno

nombre_de_la_funcion(argumentos)
"""

#Ejemplo 1
print ("----------- Ejemplo 1 -------------")
def muetra_nombre():
    print("Victor")
    print("Cinlo")
    print("Lucia")
    print("Sofia")
    print("Mateo")

muetra_nombre()

#Ejemplo 2
print ("----------- Parametros en funciones -------------")

def mostrar_nombre_y_apellido(nombre, apellido):
    print(f"Tu nombre es: {nombre} y tu apellido es: {apellido}")   
mostrar_nombre_y_apellido("Victor", "Robles")
mostrar_nombre_y_apellido("Sofia", "Garcia")

def mostrar_nombre(nombre, edad):
    print(f"tu nombre es: {nombre}")
    
    if edad >= 18:
        print("Eres mayor de edad")

nombre = input("ingresa tu nombre: ")
edad = int(input("ingresa tu edad: "))

mostrar_nombre(nombre, edad)

#Ejemplo 3
print ("----------- Ejemplo 3: Tabla multiplicar -------------")

def tabla_multiplicar(numero):
    print(f"Tabla de multiplicar del número: {numero}")
    for i in range (1,11):
        operacion = numero * i
        print(f"{numero} x {i} = {operacion}")
    return True
tabla_multiplicar(7)
tabla_multiplicar(8)

print ("----------- Ejemplo 3.1: Tabla multiplicar -------------")

for numero_tabla in range (1,11):
    tabla_multiplicar(numero_tabla)


#Ejemplo 4
print ("----------- Ejemplo 4: Parametros opcionales -------------")

def getEmpleado(nombre, dni = None):
    print("EMPLEADO")
    print(f"Nombre:  {nombre}")
    if dni != None:    
        print(f"DNI: {dni}")

getEmpleado("Cinlo Losada")

print("----------- Ejemplo 5: Parametros opcionales o devolver datos -------------")

def saludame(nombre):
    saludo = f"Hola, saludos {nombre}"
    return saludo

print(saludame("Cinlo"))

print("----------- Ejemplo 6: Funciones dentro de funciones -------------")

def calculadora(numero1, numero2, basicas = False):
    suma = numero1 + numero2
    resta = numero1 - numero2
    multi = numero1 * numero2   
    div = numero1 / numero2

    cadena = ""

    if basicas != False:
        cadena += "Suma:" + str(suma)
        cadena += "\n"
        cadena += "Resta:" + str(resta)
    else:
        cadena += "Multiplicación:" + str(multi)
        cadena += "\n"
        cadena += "División:" + str(div)
    
    return cadena

print(calculadora(10, 2))

print("----------- Ejemplo 7:Funciones dentro de otras funciones -------------")

def getNombre(nombre):
    texto = f"El nombre es: {nombre}"
    return texto

def getApellidos(apellidos):
    texto = f"Los apellidos son: {apellidos}"
    return texto

def devuelveTodo(nombre, apellidos):
    texto = getNombre(nombre) + "\n" + getApellidos(apellidos)
    return texto

print(devuelveTodo("Cinlo", "Losada"))

print("----------- Ejemplo 8: Funciones lambda -------------")

dime_el_year = lambda year: f"El año es: {year}"
print(dime_el_year(2024))
