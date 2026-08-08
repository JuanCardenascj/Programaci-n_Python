"""Instrucción:

Crea una lista de vocales: vocales = ["a", "e", "i", "o", "u"]
Pide una letra al usuario
Usa in para verificar si es una vocal
Muestra el resultado

Explicación:
letra in vocales → Verifica si la letra está en la lista
"""

vocales = ["a", "e", "i", "o", "u"]
letra = input("Letra: ").lower()

if letra in vocales:
    print("Es una vocal")
else:
    print("Es una consonante")