"""Instrucción:

Crea original = [1, 2, 3]
Crea copia = original
Agrega un elemento a copia
Muestra ambas listas

Explicación:
copia = original → No crea una nueva lista, solo crea un "alias"
Cuando modificas copia, también modificas original
"""

original = [1, 2, 3]
copia = original
copia.append(4)

print(original)
print(copia)