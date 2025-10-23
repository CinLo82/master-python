"""
#while
es una estructura de control que permite ejecutar un bloque de código mientras una condición sea verdadera.

while condición:
    # Bloque de código a repetir
    actualizar_condición()

"""

contador = 1

while contador <= 100:
    print("Voy por el número: " + str(contador))
    contador += 1  # contador = contador + 1

print("----------------------------------------")

contador = 1
muestrame = str(0)

while contador <= 100:
    muestrame += str(contador) + ", "
    contador += 1  # contador = contador + 1

print(muestrame)

print("----------------Tabla de multiplicar---------------------")

numero = int(input("Introduce un número para ver su tabla de multiplicar: "))
print("######## Tabla de multiplicar del " + str(numero) + " ########")
contador = 0
while contador <= 10:
    print(str(numero) + " x " + str(contador) + " = " + str(numero * contador))
    contador += 1
else:
    print("Tabla de multiplicar finalizada")
    