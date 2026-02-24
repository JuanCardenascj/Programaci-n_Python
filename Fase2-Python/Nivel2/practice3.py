"""
🔥 Ahora desafío real

Imagina que el programa debe:

Permitir ingresar múltiples notas.

Terminar solo cuando el usuario escriba "salir".

Al final mostrar el promedio.

¿Cómo empezarías a pensar ese problema?

No quiero código aún.
Quiero tu diseño mental paso a paso. 💪
"""

suma = 0
contador = 0

while True:
    entrada = input("Digite una nota (0 a 5) o escriba 'salir' para terminar: ")

    if entrada.lower() == "salir":
        break

    try:
        nota = float(entrada)

        if nota < 0 or nota > 5:
            print("Nota inválida. Debe estar entre 0 y 5.")
        else:
            suma += nota
            contador += 1

    except ValueError:
        print("Error: Debe ingresar un número válido.")

# Después del ciclo

if contador > 0:
    promedio = suma / contador
    print(f"Promedio final: {promedio}")
else:
    print("No se ingresaron notas válidas.")