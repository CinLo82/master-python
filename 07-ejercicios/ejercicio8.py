"""
Ejercicio 8:
"""

numero = int(input("Ingrese el num: "))
porcentaje = int(input(f"Ingrese el porcentaje que quieres sacar de {numero}:"))

operacion = (numero * (porcentaje/ 100)) 
print(f"El {porcentaje}% de {numero} es: {operacion}")