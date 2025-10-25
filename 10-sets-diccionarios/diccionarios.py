"""
Ejemplos de diccionarios en Python: definición, modificación, adición y eliminación de elementos
Un diccionario en Python es una colección de pares clave-valor, donde cada clave es única y se utiliza para acceder a su valor correspondiente. Los diccionarios son mutables, lo que significa que se pueden modificar después de su creación. Se definen utilizando llaves {} y los pares clave-valor se separan por comas. Los diccionarios son útiles para almacenar datos estructurados y permiten un acceso rápido a los valores mediante sus claves.
"""

# Definir diccionarios
print("------------ #Definir diccionarios -------------")
persona = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}
print(persona)
print(type(persona))
print(persona["nombre"])

print("------------ #diccionarios dentro de las listas -------------")

personas = [
    {"nombre": "Ana", "edad": 25},
    {"nombre": "Luis", "edad": 28},
    {"nombre": "Marta", "edad": 22}
]
print(personas)
print(personas[1]["nombre"])

contactos = [
    {
        "nombre": "Carlos", "telefono": "123456789"
    },
    {
        "nombre": "Sofia", "telefono": "98765432"
    },
    {
        "nombre": "Elena", "telefono": "555555555"
    }
]
print(contactos)

print("--------Lista de contactos---------")

for contacto in contactos:
   
    print(contacto["nombre"] + ": " + contacto["telefono"])

    print("--------------------------")
