"""
Ejercicio 1
Crea una lista con varios números enteros. Realiza las siguientes operaciones:
- Muestra todos los números de la lista.
- Ordena la lista de menor a mayor y muestra el resultado.
- Muestra la longitud de la lista.
- Permite al usuario buscar un número en la lista e indica si está presente o no.

"""

lista = [1, 2, 20, 15, 7, 3, 4, 5]

for i in lista:
    print(i)

print("------Números como strings-------")

def mostrar_lista(lista):
    resultado = ""
    for i in lista:
        resultado += "Elemento: " +  str(i) + " "
        resultado += "\n"
    return resultado
print(mostrar_lista(lista))

print("------ordenar la lista-------")

lista.sort()
print(lista)
print(mostrar_lista(lista))

print("-------Longuitud de la lista------")

print(len(lista))

print("------Buscar un elemento(que el usuario pida por teclado)-------")

busqueda = int(input("Ingrese un número a buscar en la lista: "))

comprobar = isinstance(busqueda, int)
while not comprobar or busqueda <= 0:
    busqueda = int(input("Ingrese un número válido a buscar en la lista: "))
else:
    print(f"{busqueda} no esta en la lista")

seach = lista.index(busqueda) 
print(f"El número {busqueda} se encuentra en la posición {seach} de la lista")