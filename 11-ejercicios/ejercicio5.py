"""
Ejercicio 5:
"""

tabla = [
    {
        "categoria": "Accion",
        "juegos": ["GTA", "COD", "PUGB"]
    },
    {
        "categoria": "Aventura",
        "juegos": ["ASSINS", "CRASH", "PRINCE OF PERSIA"]   
    },
    {
        "categoria": "Deporte",
        "juegos": ["FIFA", "NBA", "MOTO GP"]
    }
]

for categoria in tabla:
    print(f"-------Categoria: {categoria['categoria']}-------")
    for juego in categoria['juegos']:
        print(f"- {juego}")