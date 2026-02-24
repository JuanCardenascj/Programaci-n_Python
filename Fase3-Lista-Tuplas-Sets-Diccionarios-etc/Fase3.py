"""
Fase 3 – Pregunta 1

Supón que tienes esta lista:

numeros = [1, 2, 3, 2, 1]

Si convierto esta lista a set así:

conjunto = set(numeros)
print(conjunto)
Pregunta:

¿Qué imprime y por qué?

¿Por qué el set se comporta así?

Respóndeme razonando.
"""

numeros = [1, 2, 3, 2, 1]
conjunto = set(numeros)
print(conjunto)

#Imprime {1, 2, 3} - El set elimina los duplicados automáticamente

"""2. Por qué se comporta así:
Los sets en Python:

No permiten elementos duplicados. ✅

No mantienen un orden específico. (aunque en Python 3.7+ el orden de inserción se conserva en la mayoría de casos, no se debe confiar en ello para lógica crítica).

Permiten operaciones rápidas de búsqueda y comparación.

💡 Tip profesional:

Usa un set cuando quieras elementos únicos y búsquedas eficientes.

Usa una lista si necesitas orden y duplicados.
"""


"""Fase 3 – Pregunta 2

Supón este diccionario:

usuario = {"nombre": "Ana", "edad": 25, "activo": True}
Pregunta:

Cómo accedes al valor de "edad"?

Cómo cambias "activo" a False?

Cómo agregas un nuevo campo "ciudad": "Bogotá"?

Respóndeme razonando."""

usuario = {"nombre": "Ana", "edad": 25, "activo": True}
#Acceder 
print(usuario["edad"])

#Cambiar
usuario["activo"] = False

#Agregar
usuario["ciudad"] = "Bogota"


"""
🧠 Situación real (como sistema de usuarios)

Tienes esto:

usuarios_registrados = ["ana", "juan", "maria", "pedro"]
usuarios_activos = {"ana", "maria"}
Pregunta:

¿Cómo obtienes los usuarios que están registrados pero NO están activos?

¿Qué tipo de dato usarías para hacer esa operación más fácil?

¿Por qué no sería buena idea hacerlo solo con listas?

Respóndeme razonando, como lo vienes haciendo 💪
"""

usuarios_registrados = ["ana", "juan", "maria", "pedro"]
usuarios_activos = {"ana", "maria"}

usuarios_no_activos = set(usuarios_registrados) - usuarios_activos
print(usuarios_no_activos)

"""
1️⃣ Lista

Mantiene orden de ingreso ✅

Permite iterar en secuencia ✅

2️⃣ Set

Garantiza que no haya duplicados ✅

Operaciones de diferencia, unión e intersección ✅

3️⃣ Diccionario

Permite acceso rápido a información usando claves ✅

Ideal para búsquedas, estados de usuario, estadísticas, etc.

💡 Analogía de la vida real:

Lista → agenda ordenada

Set → lista de invitados donde no quieres repetidos

Diccionario → agenda con número de teléfono para buscar rápido
"""


# 🎯 Objetivo del programa

# Pedir nombres hasta que escriban "salir".

# No permitir duplicados → usamos set.

# Mantener orden de ingreso → usamos lista.

# Guardar estado activo/inactivo → usamos diccionario.

usuarios_orden = []        # Mantiene el orden
usuarios_unicos = set()    # Evita duplicados
usuarios_estado = {}       # Guarda activo/inactivo

while True:
    nombre = input("Ingrese un usuario o escriba 'salir': ").strip().lower()

    if nombre == "salir":
        break

    if nombre in usuarios_unicos:
        print("⚠️ Usuario ya registrado.")
        continue

    # Si no está repetido:
    usuarios_unicos.add(nombre)
    usuarios_orden.append(nombre)
    usuarios_estado[nombre] = True  # Por defecto activo

    print("✅ Usuario agregado correctamente.")

# Mostrar resultados finales
print("\n--- LISTADO FINAL ---")

for usuario in usuarios_orden:
    estado = "Activo" if usuarios_estado[usuario] else "Inactivo"
    print(f"{usuario} → {estado}")