"""
Crea una lista con 5 notas decimales.

Por ejemplo:

notas = [4.5, 3.8, 4.0, 5.0, 4.2]

Calcula:

La suma de todas las notas.
El promedio.
La nota más alta.
La nota más baja.

No uses sum(), max() ni min().
"""

#Creando una lista con las notas decimales...!

notas = [4.5, 3.8, 4.0, 5.0, 4.2]

suma = 0

for nota in notas:
    suma += nota

promedio = suma / len(notas)

mayor = notas[0]
menor = notas[0]

for nota in notas:
    if nota > mayor:
        mayor = nota

    if nota < menor:
        menor = nota

print("Suma:", suma)
print("Promedio:", promedio)
print("Mayor:", mayor)
print("Menor:", menor)