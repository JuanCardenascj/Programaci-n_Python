"""Instrucción:

Crea clima = "lluvioso"
Usa if con elif y else
Muestra un mensaje según el clima

Explicación:
elif solo se evalúa si el if anterior es falso
else se ejecuta si todas las anteriores son falsas
"""

clima = "lluvioso"

if clima == "soleado":
    print("Ve al parque")
elif clima == "lluvioso":
    print("Lleva paraguas")
else:
    print("Quédate en casa")