"""Instrucción:

Define usuario_correcto = "admin" y password_correcto = "1234"
Pide usuario y contraseña
Usa condicionales para verificar
Muestra el resultado

Explicación:
Compara con las credenciales correctas
"""

usuario_correcto = "admin"
password_correcto = "1234"

usuario = input("Usuario: ")
password = input("Contraseña: ")

if usuario == usuario_correcto and password == password_correcto:
    print("Acceso concedido")
else:
    print("Acceso denegado")