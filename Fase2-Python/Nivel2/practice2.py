"""
🎯 Nuevo reto

Escribe un programa que:

Pida la nota.

Si hay error → vuelva a pedirla.

Si está fuera de rango → vuelva a pedirla.

Solo termine cuando la nota sea válida.

Luego imprima aprobado o reprobado.

No quiero solución perfecta.
Quiero que intentes estructurarlo.

Aquí empieza el verdadero pensamiento estructural. 💪
"""

while True:
    try:
        nota = float(input("Digite una nota (0 a 5): "))

        if nota < 0 or nota > 5:
            print("Nota inválida. Debe estar entre 0 y 5.")
        else:
            break  # Sale del ciclo si es válida

    except ValueError:
        print("Error: Debe ingresar un número válido.")

# Aquí solo llega si la nota es válida

if nota >= 3:
    print("Aprobado")
else:
    print("Reprobado")