"""
LISTAS EN PYTHON
Las listas en Python son estructuras de datos que permiten almacenar múltiples valores en una sola variable. Son similares a los arrays en otros lenguajes de programación, pero con más funcionalidades y flexibilidad.
Se definen utilizando corchetes [] y los elementos se separan por comas. Las
listas pueden contener elementos de diferentes tipos de datos, como números, cadenas, booleanos, e incluso otras listas.
"""

pelicula = "Batman"

print("------------ #Definir listas -------------")

peliculas = ["Batman", "Spiderman", "El señor de los anillos"]
cantantes = list(("Keane", "Pink", "Callum Scott"))
years = list(range(2000, 2025))
variadas = [10, "Cinlo", 25.5, True, "Losada"]

print(pelicula)
print(peliculas)
print(cantantes)
print(years)

print("------------ #Acceder a elementos de la lista -------------")
print(peliculas[0])
print(peliculas[1]) 
print(peliculas[1:3])
print(cantantes[2])
print(years[5])
print(variadas[3])
print(variadas[1])
print("El año es: " + str(years[10]))
print("El cantante es: " + cantantes[0])
print("La pelicula es: " + peliculas[1])

print("------------ #Modificar elementos de la lista -------------")

peliculas[0] = "Ironman"
peliculas[1] = "Capitan America"
cantantes[2] = "Adele"
print(peliculas)
print(cantantes)
print("El año modificado es: " + str(years[10]))
years[10] = 2030
print("El año modificado es: " + str(years[10]))

print("------------ #Agregar elementos a la lista -------------")

peliculas.append("El Hobbit")
peliculas.append("Star Wars")
print(peliculas)
cantantes.append("The Weekend")
print(cantantes)
years.append(2025)
print(years)
variadas.append("Nuevo elemento")
print(variadas)
print("La lista tiene " + str(len(peliculas)) + " peliculas")
print("La lista tiene " + str(len(cantantes)) + " cantantes")
print("La lista tiene " + str(len(years)) + " años")
print("La lista tiene " + str(len(variadas)) + " elementos variados")

print("------------ #Recorrer listas -------------")

nueva_pelicula = ""
while nueva_pelicula != "parar":
    nueva_pelicula = input("Introduce una pelicula: ")
    peliculas.append(nueva_pelicula)

for pelicula in peliculas:
    print(f"{peliculas.index(pelicula)+1}. {pelicula}")

print("------------ #Listas multidimensionales -------------")

contactos = [
    [
        "Cinlo", 
        "Losada",
        38
    ],
    [
        "Ana",
        "Gomez",
        25
    ],
    [
        "Antonio",
        "Perez",
        52
    ]
]
print(contactos)
print("El contacto 1 es: " + contactos[0][0] + " " + contactos[0][1] + " de " + str(contactos[0][2]) + " años")
print("El contacto 2 es: " + contactos[1][0] + " " + contactos[1][1] + " de " + str(contactos[1][2]) + " años")
print("El contacto 3 es: " + contactos[2][0] + " " + contactos[2][1] + " de " + str(contactos[2][2]) + " años")
        
for contacto in contactos:
    for elemento in contacto:
        if contacto.index(elemento) == 0:
            print("Nombre: " + elemento)
        if contacto.index(elemento) == 1:
            print("Apellido: " + elemento)
        if contacto.index(elemento) == 2:
            print("Edad: " + str(elemento))
    print("-----")