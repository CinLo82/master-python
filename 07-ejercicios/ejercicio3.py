"""
Ejercicio 3:
Mostrar los cuadrados de los números del 1 al 60 tanto con bucle for como con bucle while

"""

contador = 0

#for
for contador in range(1,61):
    print("cuadrado de " + str(contador) + " es " + str(contador**2))

print("----------------------------------------")

#while
contador = 0
while contador <= 60:
    
    cuadrado = contador * contador
    print("cuadrado de " + str(contador) + " es " + str(cuadrado))

    contador += 1  # contador = contador + 1