"""Crea funciones para gestionar una lista de tareas:

agregar_tarea(lista, tarea) → Agrega una tarea

eliminar_tarea(lista, indice) → Elimina por índice

mostrar_tareas(lista) → Muestra todas las tareas

guardar_tareas(lista, archivo) → Guarda en JSON

cargar_tareas(archivo) → Carga desde JSON
"""

import json

def agregar_tarea(lista, tarea):
    lista.append(tarea)
    print(f"✅ Tarea agregada: {tarea}")
    return lista

def eliminar_tarea(lista, indice):
    if 0 <= indice < len(lista):
        eliminada = lista.pop(indice)
        print(f"🗑️ Tarea eliminada: {eliminada}")
    else:
        print("❌ Índice no válido")
    return lista

def mostrar_tareas(lista):
    if not lista:
        print("📝 No hay tareas")
    else:
        print("📋 LISTA DE TAREAS:")
        for i, tarea in enumerate(lista, 1):
            print(f"   {i}. {tarea}")
    return lista

def guardar_tareas(lista, archivo="tareas.json"):
    with open(archivo, "w", encoding="utf-8") as f:
        json.dump(lista, f, indent=4, ensure_ascii=False)
    print(f"💾 Tareas guardadas en {archivo}")
    return lista

def cargar_tareas(archivo="tareas.json"):
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print("📝 No hay archivo guardado")
        return []

# Uso
tareas = cargar_tareas()
tareas = agregar_tarea(tareas, "Aprender Python")
tareas = agregar_tarea(tareas, "Hacer ejercicio")
mostrar_tareas(tareas)
tareas = eliminar_tarea(tareas, 0)
mostrar_tareas(tareas)
guardar_tareas(tareas)