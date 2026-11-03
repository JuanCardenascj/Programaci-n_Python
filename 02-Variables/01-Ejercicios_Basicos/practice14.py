"""Instrucción:

Crea nombre = "Ana", edad = 25, ciudad = "Bogotá"
Muestra un mensaje usando f-string (formato con f)

Explicación:
f"..." → Permite poner variables dentro de {}
f"Hola {nombre}, tienes {edad} años" → Reemplaza {nombre} y {edad} con sus valores
"""

nombre = "Ana"
edad = 25
ciudad = "Bogotá"

mensaje = f"Hola {nombre}, tienes {edad} años y vives en {ciudad}"
print(mensaje)