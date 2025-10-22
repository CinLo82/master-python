# un condicional es una estructura de control que permite ejecutar diferentes bloques de código según si una condición es verdadera o falsa
"""
# condicional if

SI se_cimple_esta_condicion:
    ejecutar_este_bloque_de_codigo
SI_NO:
    ejecutar_este_otro_bloque_de_codigo

    if condicion:
        # bloque de código si la condición es verdadera
    else:
        # bloque de código si la condición es falsa

"""
print("############## Condicionales ##############")

#Ejemplo 1
print("-------- Ejemplo 1 ---------")

color = "rojo"

if color == "rojo":
    print("El color es rojo")
else:
    print("El color no es rojo")


#Ejemplo 2
print("-------- Ejemplo 2 ---------")

color = "azul"
if color == "rosa":
    print("Adivinaste, es mi color favorito")
else:
    print("No es mi color favorito")


print("############## Operadores de comparación ##############")

"""
# Operadores de comparación
Igual:               a == b
Distinto:           a != b
Mayor que:          a > b
Menor que:         a < b
Mayor o igual que:  a >= b
Menor o igual que:  a <= b
"""

#year = 2024
year = 2020

if year >= 2023:
    print("Estamos en el año 2023 o en un año posterior")
else:
    print("Estamos en un año anterior a 2023")

print("############## Anidacion de if ##############")

nombre = "Cinlo"
ciudad = "Madrid"
continente = "Europa"
edad = 14
mayoria_edad = 18

if edad >= mayoria_edad:
    print(f"{nombre} es mayor de edad")
    if ciudad == "Madrid":
        print("Además vive en la ciudad de Madrid")
    else:
        print("No vive en Madrid")
else:
    print(f"{nombre} es menor de edad")


print("############## Elif ##############")

#dia = int(input("Introduce el número del día de la semana (1-7): "))
dia = 5

if dia == 1:
    print("Es lunes")
else:
    if dia == 2:
        print("Es martes")
    else:
        if dia == 3:
            print("Es miércoles")
        else:
            if dia == 4:
                print("Es jueves")
            else:
                if dia == 5:
                    print("Es viernes")
                else:
                    if dia == 6:
                        print("Es sábado")
                    else:
                        if dia == 7:
                            print("Es domingo")
                        else:
                            print("Número de día no válido")

# Mejor forma con elif

if dia == 1:
    print("Es lunes")
elif dia == 2:
    print("Es martes")
elif dia == 3:
    print("Es miércoles")
elif dia == 4:
    print("Es jueves")
elif dia == 5:
    print("Es viernes")
elif dia == 6:
    print("Es sábado")          
elif dia == 7:
    print("Es domingo") 
else:
    print("Número de día no válido")    


print("############## Operadores logicos y multiples ##############")

# Operador and Y
print("---- Operador and ----")
edad_minima = 18
edad_maxima = 65
#edad_oficial = int(input("Introduce tu edad: "))
edad_oficial = 35

if edad_oficial >= edad_minima and edad_oficial <= edad_maxima:
    print("Está en edad de trabajar")
else:
    print("No está en edad de trabajar")


# Operador or O
print("---- Operador or ----")
pais = "Mexico"
if pais == "Mexico" or pais == "España" or pais == "Colombia":
    print(f"En {pais} se habla español")
else:
    print(f"En {pais} no se habla español")

# Operador not !
print("---- Operador not ----")
pais = "Alemania"
if not (pais == "España" or pais == "Mexico" or pais == "Colombia"):
    print(f"En {pais} no se habla español")
else:
    print(f"En {pais} se habla español")


print("---- Operador != ----")
pais = "Alemania"
if pais != "España" and  pais != "Mexico" and pais != "Colombia":
    print(f"En {pais} no se habla español")
else:
    print(f"En {pais} se habla español")
