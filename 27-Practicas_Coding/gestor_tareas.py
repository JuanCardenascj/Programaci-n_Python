import json

print("=== GESTOR DE TAREAS === ")

tareas = []

# Intentar cargar tareas guardadas
try:
    with open("tareas.json", "r", encoding="utf-8") as archivo:
        tareas = json.load(archivo)
    print("📂 Tareas cargadas correctamente")
except FileNotFoundError:
    print("📝 No hay archivo guardado, empezando desde cero")

while True:
    opcion = input("\n" \
    "1. Añadir tarea" \
    "\n2. Ver tareas" \
    "\n3. Salir" \
    "\nElige una opción: ")
    
    if opcion == "1":
        nueva_tarea = input("Escribe la tarea: ")
        tareas.append(nueva_tarea)
        print("¡Tarea añadida!")
    elif opcion == "2":
        if len(tareas) == 0:
            print("No hay tareas aún")
        else: 
            for i in range(len(tareas)):
                print(f"{i+1}. {tareas[i]}")
    elif opcion == "3":
        # Guardar tareas en archivo
        with open("tareas.json", "w", encoding="utf-8") as archivo:
             json.dump(tareas, archivo, indent=4, ensure_ascii=False)
             print("💾 Tareas guardadas correctamente")
        print("¡Hasta luego!")
        break  # <--- Esto sale del bucle
    else:
        print("Opción no válida")