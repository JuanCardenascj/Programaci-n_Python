"""Crea un programa que solicite:
- Nombre del jugador.
- Puntuación de la primera partida.
- Puntuación de la segunda partida.
- Puntuación de la tercera partida.

Después debe calcular y mostrar:
- Puntuación total.
- Promedio.
- Puntuación máxima.
- Puntuación mínima.
- Diferencia entre la puntuación más alta y la más baja.

Utiliza variables para almacenar todos los resultados."""

nombre_jugador = input("Ingrese el nombre del jugador: ")
puntuacion1 = float(input("Ingrese la puntuación de la primera partida: "))
puntuacion2 = float(input("Ingrese la puntuación de la segunda partida: "))
puntuacion3 = float(input("Ingrese la puntuación de la tercera partida: "))

puntuacion_total = puntuacion1 + puntuacion2 + puntuacion3
promedio = puntuacion_total / 3
puntuacion_maxima = max(puntuacion1, puntuacion2, puntuacion3)
puntuacion_minima = min(puntuacion1, puntuacion2, puntuacion3)
diferencia = puntuacion_maxima - puntuacion_minima

print(f"Nombre del jugador: {nombre_jugador}")
print(f"Puntuación total: {puntuacion_total}")
print(f"Promedio: {promedio}")
print(f"Puntuación máxima: {puntuacion_maxima}")
print(f"Puntuación mínima: {puntuacion_minima}")
print(f"Diferencia entre la puntuación más alta y la más baja: {diferencia}")