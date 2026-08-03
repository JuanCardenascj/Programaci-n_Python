"""Sin funciones para entender el concepto"""
#Crear datos
personas = [
    {"nombre": "Ana", "edad": 25},
    {"nombre": "Luis", "edad": 30},
    {"nombre": "Daniela", "edad": 30},
    {"nombre": "Zoraida", "edad": 55}
]

#Guardar en Json
import json
with open("datos.json", "w", encoding="utf-8") as archivo:
    json.dump(personas, archivo, indent=4, ensure_ascii=False)
print("Guardando")

#Leer desde json
with open("datos.json", "r", encoding="utf-8") as archivo:
    datos_leidos = json.load(archivo)
print(datos_leidos)

#Mostrar los datos
for persona in datos_leidos:
    print(f"{persona['nombre']} tiene {persona['edad']} años")


#Envolver en funciones
import json

def guardar_personas(personas, archivo="datos.json"):
    with open(archivo, "w", encoding="utf-8") as f:
        json.dump(personas, f, indent=4, ensure_ascii=False)
    print("✅ Guardado")

def cargar_personas(archivo="datos.json"):
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# USAR LAS FUNCIONES
personas = [
    {"nombre": "Ana", "edad": 25},
    {"nombre": "Luis", "edad": 30}
]

# Guardar
guardar_personas(personas)

# Cargar
datos = cargar_personas()
for persona in datos:
    print(f"{persona['nombre']} tiene {persona['edad']} años")

#Agregar Funcionalidad
import json

ARCHIVO = "datos.json"

def guardar_personas(personas):
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(personas, f, indent=4, ensure_ascii=False)
    print("✅ Guardado")

def cargar_personas():
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def agregar_persona(personas, nombre, edad):
    persona = {"nombre": nombre, "edad": edad}
    personas.append(persona)
    guardar_personas(personas)
    print(f"✅ {nombre} agregado")

def mostrar_personas(personas):
    if not personas:
        print("📝 No hay personas")
        return
    print("\n📋 PERSONAS:")
    for i, p in enumerate(personas, 1):
        print(f"  {i}. {p['nombre']} - {p['edad']} años")

# PROGRAMA PRINCIPAL
personas = cargar_personas()

while True:
    print("\n1. Ver personas")
    print("2. Agregar persona")
    print("3. Salir")
    opcion = input("Elige: ")
    
    if opcion == "1":
        mostrar_personas(personas)
    elif opcion == "2":
        nombre = input("Nombre: ")
        try:
            edad = int(input("Edad: "))
            agregar_persona(personas, nombre, edad)
        except ValueError:
            print("❌ La edad debe ser un número")
    elif opcion == "3":
        guardar_personas(personas)
        print("👋 Hasta luego")
        break
    else:
        print("❌ Opción no válida")