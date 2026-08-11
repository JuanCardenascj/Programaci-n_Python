"""Instrucción:

Pide un email
Usa condiciones para validar:
Contiene "@"
Tiene al menos un punto después del "@"
Muestra si es válido

Explicación:
@ in email → Verifica que tenga @
"." in email[email.index("@"):] → Verifica punto después del @
"""

email = input("Email: ")

if "@" in email and "." in email[email.index("@"):]:
    print("Email válido")
else:
    print("Email no válido")