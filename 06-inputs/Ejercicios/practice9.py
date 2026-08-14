"""Instrucción:

Pide el nombre y apellido por separado
Combínalos en una sola variable
Muestra el nombre completo en mayúsculas

Explicación:
nombre + " " + apellido → Combina texto
"""

nombre = input("Digite su nombre: ")
apellido = input("Digite su apellido: ")
nombre_completo = nombre + " " + apellido
print(f"SU nombre completo es: {nombre_completo.upper()}")