"""
Ejercicio 4

"""

def traducir_tipo(tipo):
    resultados = none
    if tipo == str:
        resultados = "CADENA DE TEXTO"
    elif tipo == int:
        resultados = "NUMERO ENTERO"
    elif tipo == bool:
        resultados = "BOOLEANO"
    elif tipo == list:
        resultados = "LISTA"

    return resultados


def comprobar_tipo(dato, tipo):
    test = isinstance(dato, tipo)
    resultado = ""
    if test:
        resultado = f"La variable es del tipo {traducir_tipo(tipo)}"
    else:
        resultado = f"La variable no es del tipo {tipo}"
    return resultado


mi_lista = ["hola mundo", 77]
titulo = "Master en Python"
numero = 2024
verdadero = True


print(comprobar_tipo(mi_lista, list))
print(comprobar_tipo(titulo, str))
print(comprobar_tipo(numero, int))
print(comprobar_tipo(verdadero, bool))