"""
Lista:

edades = [18, 22, 17, 25, 30, 19, 21]

Determina:

Cuántos son mayores de edad.
Cuántos son menores de edad.
La edad mayor.
La edad menor.

Sin usar max() ni min().
"""

edades = [18, 22, 17, 25, 30, 19, 21]

mayores = 0
menores = 0

edad_mayor = edades[0]
edad_menor = edades[0]

for edad in edades:

    if edad >= 18:
        mayores += 1
    else:
        menores += 1

    if edad > edad_mayor:
        edad_mayor = edad

    if edad < edad_menor:
        edad_menor = edad

print("Mayores de edad:", mayores)
print("Menores de edad:", menores)
print("Edad mayor:", edad_mayor)
print("Edad menor:", edad_menor)