"""
#FOR
for elemento in iterable:
    # Bloque de código a repetir    
    hacer_algo_con(elemento)

"""

contador = 0
resultado = 0

for contador in range(10):
    print("Voy por el número: " + str(contador))
    resultado += contador
print("El resultado es: " + str(resultado))


print("############## Bucle For ##############")
# Ejemplo tabla de multiplicar

numero = int(input("Introduce un número para ver su tabla de multiplicar: "))
print("######## Tabla de multiplicar del " + str(numero) + " ########")
for i in range(11):
    print(str(numero) + " x " + str(i) + " = " + str(numero * i))
else:
    print("Tabla de multiplicar finalizada")


