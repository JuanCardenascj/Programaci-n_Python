"""Reto: Sistema de registro de jugadores
Vas a crear un pequeño programa que registre a un jugador de League of Legends y analice sus datos.

Tu programa debe cumplir lo siguiente:
1. Solicitar el nombre del jugador.
2. Solicitar su edad.
3. Solicitar su estatura.
4. Solicitar su peso.
5. Preguntar si juega clasificatorias (True o False).
6. Convertir cada dato al tipo correspondiente.
7. Mostrar todos los datos ingresados.
8. Mostrar el tipo de dato de cada variable utilizando type().
9. Calcular el IMC del jugador con esta fórmula:
\[
IMC = \frac{peso}{estatura^2}
\]

10. Mostrar el resultado del IMC con dos decimales.

Condiciones:
- Utiliza variables.
- Utiliza input().
- Utiliza conversiones de tipos.
- Utiliza type().
- No utilices clases ni funciones todavía."""

print("Bienvenido al sistema de registro de jugadores de League of Legends.....!!")

nombre = input("Por favor, ingresa tu nombre: ")
edad = int(input("Por favor, ingresa tu edad: "))
estatura = float(input("Por favor, ingresa tu estatura en metros (ejemplo: 1.75): "))
peso = float(input("Por favor, ingresa tu peso en kilogramos (ejemplo: 70.5): "))
juega_clasificatorias = input("¿Juegas clasificatorias? (True/False): ")

if juega_clasificatorias.lower() == 'true':
    juega_clasificatorias = True
else:
    juega_clasificatorias = False

print("\n¡Gracias por registrarte! Aquí están tus datos:")
print(f"Nombre: {nombre} (Tipo: {type(nombre)})")
print(f"Edad: {edad} (Tipo: {type(edad)})")
print(f"Estatura: {estatura} (Tipo: {type(estatura)})")
print(f"Peso: {peso} (Tipo: {type(peso)})")
print(f"Juega clasificatorias: {juega_clasificatorias} (Tipo: {type(juega_clasificatorias)})")

imc = peso / (estatura ** 2)
print(f"\nTu IMC es: {imc:.2f}")