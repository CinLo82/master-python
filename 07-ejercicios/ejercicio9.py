"""
Ejercicio 9: hacer un programa que pida numeros al usuario infinitamente  hasta que meta el numero 111
"""


numero = int(input("Adivina el num correcto: "))

while numero != 111:
    print("Num incorrecto")
    numero = int(input("Num incorrecto, intenta de nuevo: ")) 
print("Felicidades, has adivinado el num")