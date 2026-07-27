import json

print(" ==== BIENVENIDOS A SU GESTIONES DE INVENTARIOS S.A.S ==== \n")

# Intentar cargar productos guardados
try:
    with open("inventario.json", "r", encoding="utf-8") as archivo:
        productos_inventario = json.load(archivo)
    print("📂 Inventario cargado correctamente\n")
except FileNotFoundError:
    # Si no hay archivo, usar diccionario por defecto
    productos_inventario = {
        "Neveras": 5, 
        "Lavadoras": 19, 
        "Secadores": 12, 
        "Licuadoras": 10, 
        "Ventiladores": 32, 
        "Tejetelas": 120, 
        "Picadoras": 21, 
        "Quemadores": 321, 
        "Multidiversas": 21, 
        "Secadoras": 32, 
        "Monitores": 21, 
        "Radios": 32, 
        "Auriculares": 32, 
        "Video Consola": 30, 
        "Equipos Musicales": 2
    }
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
            # Recorrer el diccionario
            for i, (producto, cantidad) in enumerate(productos_inventario.items(), 1):
                print(f"{i}. {producto}: {cantidad} unidades")
                
    elif opciones == "2":
        nuevo_producto = input("Escriba el producto que deseas añadir al inventario: ")
        # Verificar si ya existe
        if nuevo_producto in productos_inventario:
            print(f"⚠️ El producto '{nuevo_producto}' ya existe en el inventario")
            opcion_cantidad = input("¿Quieres aumentar la cantidad? (s/n): ")
            if opcion_cantidad.lower() == "s":
                try:
                    cantidad_extra = int(input("¿Cuántas unidades quieres añadir?: "))
                    productos_inventario[nuevo_producto] += cantidad_extra
                    print(f"✅ Ahora hay {productos_inventario[nuevo_producto]} unidades de '{nuevo_producto}'")
                except ValueError:
                    print("❌ Debes ingresar un número válido")
        else:
            # Si es nuevo, pedir cantidad
            try:
                cantidad = int(input(f"¿Cuántas unidades de '{nuevo_producto}' quieres añadir?: "))
                productos_inventario[nuevo_producto] = cantidad
                print(f"✅ Producto '{nuevo_producto}' añadido con {cantidad} unidades")
            except ValueError:
                print("❌ Debes ingresar un número válido")
        
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
            # Mostrar productos con índice
            lista_productos = list(productos_inventario.keys())
            for i, producto in enumerate(lista_productos, 1):
                print(f"{i}. {producto}: {productos_inventario[producto]} unidades")
            
            try:
                num = int(input("¿Qué producto quieres eliminar? (número): "))
                if 1 <= num <= len(lista_productos):
                    producto_eliminar = lista_productos[num-1]
                    del productos_inventario[producto_eliminar]
                    print(f"✅ Producto eliminado: {producto_eliminar}")
                else:
                    print("❌ Número no válido")
            except ValueError:
                print("❌ Debes ingresar un número")
                
    elif opciones == "5":
        busqueda = input("Escribe el producto a buscar: ")
        # Buscar en las claves del diccionario
        encontrados = {p: c for p, c in productos_inventario.items() if busqueda.lower() in p.lower()}
        if encontrados:
            print(f"🔍 Productos encontrados ({len(encontrados)}):")
            for producto, cantidad in encontrados.items():
                print(f"  - {producto}: {cantidad} unidades")
        else:
            print("❌ No se encontraron productos")
    
    else:
        print("❌ Opción no válida")