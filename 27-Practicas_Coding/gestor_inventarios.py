import json

print(" ==== BIENVENIDOS A SU GESTIONES DE INVENTARIOS ORPA S.A.S ==== \n")

# Intentar cargar productos guardados
try:
    with open("inventario.json", "r", encoding="utf-8") as archivo:
        productos_inventario = json.load(archivo)
    print("📂 Inventario cargado correctamente\n")
except FileNotFoundError:
    # Si no hay archivo, usar lista por defecto
    productos_inventario = ["Neveras", "Lavadora x 12lb", "Lavadora x 16lb", "Lavadora x 25lb", "Licuadoras", "Aire BTU"]
    print("📝 No hay archivo guardado, usando inventario por defecto\n")

print("Hola ORPA S.A.S")

while True:
    print("Elija una de las siguientes opciones:")
    opciones = input("\n" \
    "1. Ver productos disponibles en el inventario\n" \
    "2. Añadir productos al inventario\n" \
    "3. Salir\n" \
    "4. Eliminar productos\n" \
    "5. Buscar productos\n" \
    "Elige una opción: ")

    if opciones == "1":
        if len(productos_inventario) == 0:
            print("No hay productos asignados en el inventario")
        else:
            print("Los productos disponibles en inventario: ")
            for i in range(len(productos_inventario)):
                print(f"{i+1}. {productos_inventario[i]}")
                
    elif opciones == "2":
        nuevo_producto = input("Escriba el producto que deseas añadir al inventario: ")
        productos_inventario.append(nuevo_producto)
        print("¡Producto añadido correctamente!\n")
        
    elif opciones == "3":
        with open("inventario.json", "w", encoding="utf-8") as archivo:
            json.dump(productos_inventario, archivo, indent=4, ensure_ascii=False)
        print("💾 Inventario guardado correctamente")
        print("Hasta luego")
        break
        
    elif opciones == "4":
        if len(productos_inventario) == 0:
            print("No hay productos para eliminar")
        else:
            print("Productos en inventario:")
            for i in range(len(productos_inventario)):
                print(f"{i+1}. {productos_inventario[i]}")
            try:
                num = int(input("¿Qué producto quieres eliminar? (número): "))
                if 1 <= num <= len(productos_inventario):
                    eliminado = productos_inventario.pop(num-1)
                    print(f"✅ Producto eliminado: {eliminado}")
                else:
                    print("❌ Número no válido")
            except ValueError:
                print("❌ Debes ingresar un número")
                
    elif opciones == "5":
        busqueda = input("Escribe el producto a buscar: ")
        encontrados = [p for p in productos_inventario if busqueda.lower() in p.lower()]
        if encontrados:
            print(f"🔍 Productos encontrados ({len(encontrados)}):")
            for p in encontrados:
                print(f"  - {p}")
        else:
            print("❌ No se encontraron productos")
    
    else:
        print("❌ Opción no válida")