"""
Ejercicio 4:
Realizar las cuatro operaciones básicas (suma, resta, multiplicación y división) con dos números ingresados por el usuario

"""

numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))

print("------------------ Suma ----------------------")

suma = numero1 + numero2
print("La suma de " + str(numero1) + " y " + str(numero2) + " es: " + str(suma))

print("------------------ Resta ----------------------")

resta = numero1 - numero2
print("La resta de " + str(numero1) + " y " + str(numero2) + " es: " + str(resta))

print("----------------- Multiplicacion -----------------------")

multiplicacion = numero1 * numero2
print("La multiplicacion de " + str(numero1) + " y " + str(numero2) + " es: " + str(multiplicacion))

print("-------------- Division --------------------------")

division = numero1 / numero2
print("La division de " + str(numero1) + " y " + str(numero2) + " es: " + str(division))