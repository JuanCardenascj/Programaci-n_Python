"""Instrucción:

Define usuario = "admin" y password = "1234"
Pide usuario y contraseña
Verifica si coinciden
Muestra acceso concedido o denegado

Explicación:
Compara las entradas con los valores definidos
"""

usuario = "admin" 
password = "1234"

usuario_ingreso = input("Digite su usuario: ")
password_ingreso = input("Digite su contraseña: ")

if usuario_ingreso == usuario and password_ingreso == password:
    print("Acceso concedido")
else:
    print("Acceso denegado")