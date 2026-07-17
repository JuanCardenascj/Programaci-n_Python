import json

print(" Bienvenido Estudiante -- Gestión de Materias\n")
saludo = input("DIGITE SU NOMBRE: ")

materias = []

try:
    with open("tareas.json", "r", encoding="utf-8") as archivo:
        materias = json.load(archivo)
    print("📂 Tareas cargadas correctamente")
except FileNotFoundError:
    print("📝 No hay archivo guardado, empezando desde cero")

while True:
    print(f"\nHola {saludo}\n Elija una de las siguientes opciones: :D")
    opciones = input("\n" \
    "1. Añadir una nueva materia\n" \
    "2. Ver materias actuales\n" \
    "3. Salir\n" \
    "------>>\n ")

    if opciones == "1":
        nueva_materia = input("Escriba la materia que desea añadir: ")
        materias.append(nueva_materia)
        print("¡Materia añadida correctamente!\n")
    elif opciones == "2":
        if len(materias) == 0:
            print("No hay materias asignadas aún")
        else: 
            print("Las materias añadidas son: ")
            for i in range(len(materias)):
                print(f"{i+1}. {materias[i]}")
    elif opciones == "3":
        with open("materias.json", "w",
                  encoding="utf-8") as archivo:
            json.dump(materias, archivo, indent=4, ensure_ascii=False)
            print("Tareas guardadas correctamente!")
        print("¡Hasta luego!")
        break #-->Salir del bucle
    else:
        print("Opcion no válida")