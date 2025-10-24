cantantes = ["Linkin Park", "Metallica", "Coldplay", "Imagine Dragons"]
numeros = [1, 2, 5, 3, 8, 7, 4, 6]

# Ordenar listas
print("------------ #Ordenar listas -------------")
cantantes.sort()
numeros.sort()
print(cantantes)
print(numeros)

print("------------ #Añadir elementos en la listas -------------")

cantantes.append("Roxette")
cantantes.insert(2, "Green Day")
numeros.append(10)
print(cantantes)
print(numeros)

print("------------ #Eliminar elementos en la listas -------------")

cantantes.remove("Coldplay")
numeros.pop()  # Elimina el último elemento
numeros.pop(2)  # Elimina el elemento en la posición 2
print(cantantes)
print(numeros)

print("------------ #Dar vuelta elementos en la listas -------------")

numeros.reverse()
print(numeros)

print("------------ #Buscar elementos en la listas -------------")

print("Green Day" in cantantes)

pos = cantantes.index("Green Day")
print("Green Day está en la posición: " + str(pos))

print("------------ #Contar elementos en la listas -------------")

print(len(cantantes))

print("------------ #Contar Cuantas veces aparece un elemento en la lista-------------")

print(cantantes.count("Metallica"))

print("------------ #Buscar los indices de un elemento -------------")

for i, cantante in enumerate(cantantes):
    print(f"{i}. {cantante}")

print("----")
print(cantantes.index("Metallica"))

print("------------ #Unir listas -------------")

nueva_lista = cantantes + numeros
print(nueva_lista)


