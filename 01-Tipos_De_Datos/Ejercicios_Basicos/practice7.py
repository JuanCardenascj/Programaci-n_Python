"""
Crea una tupla llamada colores con 4 colores.

Muestra:

La tupla completa
El segundo color
"""

#Creando una tupla llamada colores con 4 colores -> Variable colores
colores = ("Amarillo", "Rojo", "Azul", "Naranja")

#Imprimiendo la tupla completa
print(colores)

#Imprimiento solo el segundo color
print(colores[1])

"""
Crea una tupla con:

10, 20, 30, 40

Muestra el primer número.
"""

#Creando la tupla..!
tupla = 10, 20, 30, 40

#Mostrando el primero número
print(tupla[0])

#Recorriendo la tupla
for tuple in tupla:
    print(tuple)

#Verificando si el número 20 existe en la tupla
if 20 in tupla:
    print("Si existe!")