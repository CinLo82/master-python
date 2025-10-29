"""
Ejercicio 3
Crea una variable vacía y comprueba su valor. Si está vacía, pide al usuario que
ingrese un texto para llenarla y luego muestra el contenido en mayúsculas.
"""

texto = ""

len(texto) == 0 
    
print("La variable texto esta vacia")

if texto == "":
    texto = input("Ingrese un texto para la variable vacia: ")
    print("La variable texto ahora tiene contenido:", texto.upper())


cinlo = ""
if len(cinlo) <= 0:
    cinlo = "Cinlo Losada"
    print("La variable cinlo ahora tiene contenido:", cinlo.upper())
 
else:
    print("La variable cinlo tiene contenido:", cinlo.upper())