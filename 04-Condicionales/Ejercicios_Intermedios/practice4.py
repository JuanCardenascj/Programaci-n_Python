"""Instrucción:

Usa condiciones para verificar:
Longitud de al menos 8 caracteres
Contiene al menos un número
Muestra si es válida o no

Explicación:
len(password) >= 8 → Longitud
any(char.isdigit() for char in password) → Verifica si hay algún número
"""
password = input("Contraseña: ")

if len(password) >= 8 and any(char.isdigit() for char in password):
    print("Contraseña válida")
else:
    print("Contraseña no válida")