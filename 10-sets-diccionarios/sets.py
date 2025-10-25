"""
SETS EN PYTHON
Los sets en Python son colecciones desordenadas de elementos únicos. A diferencia de las listas o tuplas, los sets no permiten elementos duplicados y no mantienen un orden específico. Se definen utilizando llaves {} o la función set(). Los sets son útiles cuando se necesita almacenar elementos sin duplicados y realizar operaciones matemáticas como uniones, intersecciones y diferencias entre conjuntos.    

"""
# Definir sets
print("------------ #Definir sets -------------")
frutas = {"manzana", "banana", "naranja", "pera"}
numeros = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
mixto = {1, "dos", 3.0, True, "cinco"}

print(frutas)
print(numeros)
print(mixto)

frutas.add("kiwi")
print(frutas)
numeros.remove(1)
print(numeros)

print(type(frutas))
print(type(numeros))
print(type(mixto))