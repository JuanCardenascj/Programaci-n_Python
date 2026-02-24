"""FASE 1:
   Tipos de datos y operaciones básicas.!

1️⃣ Conceptos clave
Números: int (enteros), float (decimales)
Cadenas: str (texto)
Booleanos: True / False
Operaciones: + - * / // % **
"""

#Ejemplo....!

a = 5 #Entero o Integer or Int
b = 3.52 #Float o Flotante or Decimal
c = "Hey, daddy" #Str o Cadena
d = True #Booleano

print(a + b) #8.52 resultado flotante o float
print(c + " babby") #Hey, daddy babby

"""2️⃣ Preguntas de razonamiento"""
#Si hago:

# x = "5"
# y = 3
# print(x + y) 

#No se puede sumar una cadena con un entero directamente - resultado TypeError

"""2️⃣ Preguntas de razonamiento
Crea un programa que pida dos números al usuario y muestre:

Suma
Resta
Multiplicación
División
División entera
Módulo
"""

num1 = int(input("Digite un numero"))
num2 = int(input("Digite un numero"))

suma = num1 + num2
multiplicación = num1 * num2
resta = num1 -  num2
division = num1 / num2
division_entera = num1 // num2
modulo_residuo = num1 % num2

print(suma,multiplicación, resta, division, division_entera, modulo_residuo)