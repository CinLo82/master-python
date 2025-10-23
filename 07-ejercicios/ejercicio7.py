"""
Ejercicio 7: Hacer un programa que muestre los números pares entre dos números
ingresados por el usuario

"""

numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

if numero1 < numero2:
    for i in range(numero1, (numero2 + 1)):
        resultado = i % 2
        if resultado == 0:
            print(f" {i} es par")
        else:
            print(f" {i} es impar")
# si el numero no es menor

else:
    print("El primer número debe ser menor al segundo número")
