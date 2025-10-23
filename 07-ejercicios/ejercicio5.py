"""
Ejercicio 5: Números entre dos enteros positivos
Escribir un programa que solicite al usuario dos números enteros positivos y
muestre en pantalla todos los números enteros comprendidos entre ellos (incluyendo  
los números ingresados).
"""

numero1 = int(input("Ingrese un número entero positivo: "))
numero2 = int(input("Ingrese otro número entero positivo: "))

# si ek numero1 es mayor que numero2, intercambiamos sus valores
if numero1 > numero2:
    numero1, numero2 = numero2, numero1
# imprimimos los números entre numero1 y numero2 (inclusive)
for i in range(numero1, numero2 + 1):
    print(i)
