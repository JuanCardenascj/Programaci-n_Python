"""🧠 Reto: Sistema de estadísticas de un jugador de League of Legends
Dificultad: intermedia
Vas a crear un programa que registre las estadísticas de un jugador durante 5 partidas.
Tu programa debe cumplir estos requisitos:
1. Solicitar el nombre del jugador.
2. Solicitar su campeón favorito.
3. Registrar cuántas partidas ganó.
4. Registrar cuántas partidas perdió.
5. Registrar cuántas asistencias consiguió en cada una de las 5 partidas.
6. Calcular el total de asistencias.
7. Calcular el promedio de asistencias.
8. Calcular el porcentaje de victorias.
9. Mostrar todas las estadísticas.

Condiciones
- Utiliza input().
- Utiliza int() y float() cuando corresponda.
- Utiliza una lista para almacenar las asistencias.
- Utiliza operaciones matemáticas.
- Utiliza type() para mostrar los tipos de datos.
- No utilices clases ni funciones todavía.

Ejemplo de cómo debería verse el resultado
Si registras:
- Jugador: Juand
- Campeón: Yasuo
- Victorias: 3
- Derrotas: 2
- Asistencias: 5, 8, 3, 10, 4

El resultado debería incluir:
Jugador: Juand
Campeón favorito: Yasuo
Partidas jugadas: 5
Victorias: 3
Derrotas: 2
Total de asistencias: 30
Promedio de asistencias: 6.0
Porcentaje de victorias: 60%


Una regla: no copies el ejemplo como código. Construye el programa desde cero."""

print("Bienvenido al sistema de estadísticas de un jugador de League of Legends.....!!")
nombre = input("Por favor, ingresa tu nombre: ")
campeon_favorito = input("Por favor, ingresa tu campeón favorito: ")
victorias = int(input("Por favor, ingresa cuántas partidas ganaste: "))
derrotas = int(input("Por favor, ingresa cuántas partidas perdiste: "))
asistencias = []
for i in range(5):
    asistencia = int(input(f"Por favor, ingresa las asistencias para la partida {i+1}: "))
    asistencias.append(asistencia)
    
total_asistencias = sum(asistencias)
promedio_asistencias = total_asistencias / len(asistencias)
partidas_jugadas = victorias + derrotas
porcentaje_victorias = (victorias / partidas_jugadas) * 100 if partidas_jugadas > 0 else 0

print(f"\nJugador: {nombre}")
print(f"Campeón favorito: {campeon_favorito}")
print(f"Partidas jugadas: {partidas_jugadas}")
print(f"Victorias: {victorias}")
print(f"Derrotas: {derrotas}")
print(f"Total de asistencias: {total_asistencias}")
print(f"Promedio de asistencias: {promedio_asistencias:.1f}")
print(f"Porcentaje de victorias: {porcentaje_victorias:.0f}%")