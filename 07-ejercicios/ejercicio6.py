"""
Ejercicio 6: Mostrar tablas de multiplicar
Escribir un programa que muestre las tablas de multiplicar del 1 al 10.
Mostando el tirulo de la tabla y luego los resultados de la tabla.

"""

print("-------------------- Tabla del 1 -----------------------")

contador = 1
resultado = 1

for i in range(11):
    resultado = contador * i
    print( str(contador) + " x " + str(i) + " es: " + str(resultado))   
    
print("-------------------- Tabla del 2 -----------------------")

contador = 2
resultado = 1

for i in range(11):
    resultado = contador * i
    print( str(contador) + " x " + str(i) + " es: " + str(resultado))   
    
print("-------------------- Tabla del 3 -----------------------")

contador = 3
resultado = 1

for i in range(11):
    resultado = contador * i
    print( str(contador) + " x " + str(i) + " es: " + str(resultado))   
    
print("-------------------- Tabla del 4 -----------------------")

contador = 4
resultado = 1

for i in range(11):
    resultado = contador * i
    print( str(contador) + " x " + str(i) + " es: " + str(resultado))   

print("-------------------- Tabla del 5 -----------------------")

contador = 5
resultado = 1
for i in range(11):
    resultado = contador * i
    print( str(contador) + " x " + str(i) + " es: " + str(resultado))

print("-------------------- Tabla del 6 -----------------------")

contador = 6
resultado = 1
for i in range(11):
    resultado = contador * i
    print( str(contador) + " x " + str(i) + " es: " + str(resultado))

print("-------------------- Tabla del 7 -----------------------")

contador = 7
resultado = 1   
for i in range(11):
    resultado = contador * i
    print( str(contador) + " x " + str(i) + " es: " + str(resultado))

print("-------------------- Tabla del 8 -----------------------")

contador = 8
resultado = 1

for i in range(11):
    resultado = contador * i
    print( str(contador) + " x " + str(i) + " es: " + str(resultado))
    
print("-------------------- Tabla del 9 -----------------------")

contador = 9
resultado = 1

for i in range(11):
    resultado = contador * i
    print( str(contador) + " x " + str(i) + " es: " + str(resultado))
print("-------------------- Tabla del 10 -----------------------")

contador = 10
resultado = 1

for i in range(11):
    resultado = contador * i
    print( str(contador) + " x " + str(i) + " es: " + str(resultado))

print("################# Fin del programa ####################")


#forma corta

for contador in range(1,11):
    print("-------------------- Tabla del " + str(contador) + " -----------------------")
    for i in range(11):
        resultado = contador * i
        print( str(contador) + " x " + str(i) + " es: " + str(resultado))
        
