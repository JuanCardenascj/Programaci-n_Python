"""Permite extraer cadenas mas grande de la cadena principal

Aplica para:

   1. Listas
   2. Tuplas
   3. Otro tipo de frecuencias"""

cadena = "Hola, gente!"
telefono = "4-5-6-4-3-4-7-9"
telefono2 = "-4-5-6-4-3-4-7-9"
print(cadena[0:4]) #Desde la posición 0 hasta la posición 4
print(cadena[6:11])
print(cadena[::2]) #Salta de dos en dos por cada letra
print(telefono[::2]) #Extra el numero de telefono sin los guiones
print(telefono2[1::2]) #Extra el numero de telefono sin los guines (Inicia desde la posición 1 y salta de 2 en 2)