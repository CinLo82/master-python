"""
Varable local y variable global en funciones
Una variable local es aquella que se define dentro de una función y solo puede ser utilizada dentro de esa función.
Una variable global es aquella que se define fuera de cualquier función y puede ser utilizada en cualquier parte

"""

#Variable global
frase = "Ni los genios son tan genios, ni los mediocres son tan mediocres"
print(frase)
def hola_mundo():
    #Variable local
    frase = "Hola mundo"
    print(frase)
    
    year = 2024
    print(year)
    return "Hola mundo desde la función"

    global website
    website = "cinlodev.com"
    print("Dentro: ", website)

hola_mundo()
print(frase)
