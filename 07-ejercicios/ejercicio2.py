"""
Ejercicio 2:
Mostrar los números pares del 1 al 120 utilizando un bucle for

"""

contador = 1

for contador in range(1,121):
    if contador % 2 == 0:
        print("El número " + str(contador) + " es PAR")
