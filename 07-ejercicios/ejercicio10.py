"""
Ejercicio 10: el programa tiene q pedir las notas de 15 alumnos y decir cuantos han aprobado y cuantos han suspendido

"""

contador = 0
aprobados = 0
suspendidos = 0

numero_alumnos = int(input("Ingrese la cantidad de alumnos: "))

while contador <= (numero_alumnos - 1):
    nota = float(input(f"Ingrese la nota del alumno {contador + 1}: "))
    if nota >= 5:
        aprobados += 1
    else:
        suspendidos += 1
    contador += 1
print(f"Alumnos aprobados: {aprobados}")
print(f"Alumnos suspendidos: {suspendidos}")
print("Fin del programa")
