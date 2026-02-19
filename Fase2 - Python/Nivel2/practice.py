# 🚀 Ahora subimos el nivel
# Quiero que escribas un programa que:

# Pida una nota.
# Si el usuario escribe algo inválido (letras, vacío, etc.), muestre error.
# Si es válido, valide rango (0–5).
# Si está fuera de rango → "Nota inválida".
# Si está en rango:
# ≥ 3 → "Aprobado"
# < 3 → "Reprobado"
# El programa NO debe explotar nunca.

# Escríbelo tú.
# Ahora sí estamos programando como desarrolladores reales. 💪

try:
    nota = int(input("Digite una nota (0, 5): "))
    if nota < 0 or nota > 5:
        print("Nota inválida. Solo se permiten valores entre 0 y 5.")
    elif nota >= 3:
        print("Aprobado")
    else:
        print("Reprobado")
except ValueError:
    print("Error: Intente nuevamente.!!!")