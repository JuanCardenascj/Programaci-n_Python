"""
Vamos a crear un mini sistema de notas usando listas y diccionarios:

Pedir al usuario varias notas (usa la función que ya hicimos para validar).

Guardarlas en una lista.

Calcular:

Promedio

Nota máxima

Nota mínima

Analizar cada nota (positivo/negativo, aprobado/reprobado).

Esto combina todo lo que ya sabes, y te prepara para estructuras más complejas en Fase 4.
"""

# -----------------------------
# Función para pedir un número dentro de un rango
# -----------------------------
def pedir_numero_rango(mensaje, min_val=0, max_val=5):
    while True:
        entrada = input(mensaje)
        if entrada.lower().strip() == "salir":
            return None  # Permite salir del programa
        try:
            numero = float(entrada)
            if min_val <= numero <= max_val:
                return numero
            else:
                print(f"Nota inválida. Debe estar entre {min_val} y {max_val}.")
        except ValueError:
            print("Error: Debe ingresar un número válido.")

# -----------------------------
# Función para analizar el número
# -----------------------------
def analizar_numero(numero):
    if numero > 0:
        return "Positivo"
    elif numero < 0:
        return "Negativo"
    else:
        return "Cero"

# -----------------------------
# Función para calcular estadísticas
# -----------------------------
def calcular_estadisticas(notas):
    promedio = sum(notas) / len(notas)
    nota_max = max(notas)
    nota_min = min(notas)
    return promedio, nota_max, nota_min

# -----------------------------
# Función para mostrar análisis de notas
# -----------------------------
def mostrar_notas(notas):
    for nota in notas:
        resultado = analizar_numero(nota)
        estado = "Aprobado ✅" if nota >= 3 else "Reprobado ❌"
        print(f"Nota: {nota} → {resultado}, Estado: {estado}")

# -----------------------------
# Programa principal
# -----------------------------
def main():
    notas = []

    # Pedir varias notas al usuario
    while True:
        nota = pedir_numero_rango("Digite una nota (0 a 5) o 'salir': ")
        if nota is None:
            break
        notas.append(nota)

    if notas:
        print("\n--- Notas ingresadas ---")
        print(notas)

        # Estadísticas
        promedio, nota_max, nota_min = calcular_estadisticas(notas)
        print(f"\nPromedio de las notas: {promedio:.2f}")
        print(f"Nota máxima: {nota_max}")
        print(f"Nota mínima: {nota_min}")

        # Mostrar análisis individual
        print("\n--- Análisis de cada nota ---")
        mostrar_notas(notas)
    else:
        print("No se ingresaron notas. Programa terminado.")

# -----------------------------
# Ejecutar el programa
# -----------------------------
if __name__ == "__main__":
    main()