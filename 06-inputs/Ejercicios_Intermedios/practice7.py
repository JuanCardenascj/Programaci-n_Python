"""Instrucción:

Pide un email al usuario
Verifica que contenga "@"
Verifica que tenga un punto después del "@"
Muestra si es válido o no

Explicación:
@ in email → Verifica que tenga @
"." in email[email.index("@"):] → Verifica punto después del @
"""

email = input("Email: ")

if "@" in email and "." in email[email.index("@"):]:
    print("Email válido")
else:
    print("Email no válido")