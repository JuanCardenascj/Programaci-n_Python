"""
Encuentra el número mayor de:

numeros = [12, 45, 7, 89, 34]

Sin usar max().
"""

numeros = [12, 45, 7, 89, 34]

mayor = numeros[0]

for numero in numeros:
    if numero > mayor:
        mayor = numero
print(f"El numero mayor es: {mayor}")