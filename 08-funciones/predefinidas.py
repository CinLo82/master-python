nombre = "Cinlo Losada"

print("------------ #Funciones generales -------------")

print(type(nombre))

print("------------ #detectar el tipado -------------")

comprobar = isinstance(nombre, str)
if comprobar:
    print("Efectivamente es una cadena")
else:
    print("No es una cadena")

if not isinstance(nombre, float):
    print("La variable no es un numero con decimales")

print("------------ #Limpiar espacios -------------")

frase = "   mi contenido   "
print(frase)
print(frase.strip())

print("------------ #Eliminar variables -------------")

year = 2024
print(year)
del year
# print(year) #Error, la variable no existe

print("------------ #Comprobar variables vacias -------------")

texto = ""
if len(texto) == 0:
    print("La variable esta vacia")
else:
    print("La variable tiene contenido")
if texto == "":
    print("La variable esta vacia")

print("------------ #Encontrar caracteres -------------")

frase = "Hola mi nombre es Cinlo Losada"
print(frase.find("Cinlo"))
print(frase.find("cinlo")) #No lo encuentra, devuelve -1
print(frase.index("Cinlo"))
# print(frase.index("cinlo")) #Error porque no lo encuentra

print("------------ #Reemplazar palabras -------------")

nueva_frase = frase.replace("Cinlo", "Victor")
print(nueva_frase)
print(frase)

print("------------ #Mayusculas y minusculas -------------")

print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
print(frase.swapcase())

print("------------ #Contar caracteres -------------")