"""Crea una función que:
1. Reciba una lista de nombre
2. Los guarde en un archivo "nombre.txt", uno por línea"""

def guardar_nombres(nombres, archivo="nombres.txt"):
    with open(archivo, "w", encoding="utf-8") as f:
        for nombre in nombres:
            f.write(nombre + "\n")
    print(f"✅ {len(nombres)} nombres guardados en {archivo}")

guardar_nombres(["Ana", "Luis", "Carlos"])