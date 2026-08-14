"""Instrucción:

Define password = "1234"
Pide la contraseña al usuario
Si es correcta, muestra "Acceso concedido"
Si no es correcta, muestra "Acceso denegado"
Usa un bucle para dar 3 intentos

Explicación:
while para repetir hasta 3 intentos
"""

password_correcta = "1234"
intentos = 3

while intentos > 0:
    password = input("Contraseña: ")
    
    if password == password_correcta:
        print("✅ Acceso concedido")
        break
    else:
        intentos -= 1
        if intentos > 0:
            print(f"❌ Contraseña incorrecta. Te quedan {intentos} intentos")
        else:
            print("❌ Acceso bloqueado")