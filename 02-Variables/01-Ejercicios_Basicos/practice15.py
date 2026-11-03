"""🟢 Básicos
1. Ficha personal

Crea variables para almacenar:
- Nombre.
- Edad.
- País.
- Estatura.
- Si estudias Python (True o False).
Muestra todos los datos utilizando print() e indica el tipo de cada variable con type()."""

nombre = input("Por favor, ingrese su nombre: ")
edad = int(input("Por favor, ingrese su edad: "))
pais = input("Por favor, ingrese su país: ")
estudias = input("¿Estudias Python? (True/False): ")

print(f" Hola {nombre}, tienes {edad} años, eres de {pais}, y estudias python: {estudias}")