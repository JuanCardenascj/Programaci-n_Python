"""QUE ES UNA FUNCIÓN:

Es como una receta de cocina. Tiene nombre, recibe ingredientes o instrucciónes y devuelve un resultado...!"""

#FUNCIONES SIMPLES EJEMPLOS.........................
#Ejemplo 1:
def saludar(nombre): #Nombre -> Parametro que recibe
    return f"Hola, como te encuentras el dia de hoy {nombre}"
mensaje = saludar("Anderson Jiménez")
print(mensaje)

#Ejemplo 2: Función que Suma Dos Números
def sumar(a, b):
    return a + b
print(sumar(12, 4))

#Ejemplo 3: Función que Multiplica
def multiplicar(a, b):
    return a * b
print(multiplicar(43, 2))

#Ejemplo 4:Función con varios parámetros
def presentar(nombre, edad, ciudad):
    return f"Hola me llamo {nombre}, tengo {edad} años y vivo en {ciudad}"
print(presentar("David Juan", 30, "Arauca-Arauca"))


#FUNCIONES CON VALORES POR DEFECTO......................
#Ejemplo 1: Saludo con masaje personalizado
def saludar_personalizado(nombre, mensaje="Hola"):
    return f"{mensaje}, {nombre}"
print(saludar_personalizado("Ana")) #Sino le asignas algo a mensaje, imprime hola por defecto
print(saludar_personalizado("Luis", "Buenos Dias"))

#Ejemplo 2: Descuento con porcentaje predeterminado
def aplicar_descuento(precio, descuento=10):
    return precio - (precio * descuento / 100)
print(aplicar_descuento(100))      # 90 (descuento 10% por defecto)
print(aplicar_descuento(100, 20))  # 80 (descuento 20%)


#FUNCIONES CON MÚLTIPLES RETORNOS......................
#Ejemplo 1: Calcular área y perímetro
def rectangulo(base, altura):
    area = base * altura #Crea la variable area
    perimetro = 2 * (base + altura) #Crea la variable perimetro
    return area, perimetro 

#Recibir ambos valores
area, perimetro = rectangulo(20, 3) #Llama la función e ingresa los valores
print(f"Área: {area}")        
print(f"Perímetro: {perimetro}")

#Ejemplo 2: Función que devuelve un diccionario
def analizar_numero(numero):
    return {
        'numero': numero,
        'cuadrado': numero ** 2,
        'cubo': numero ** 3,
        'mitad': numero / 2
    }

resultado = analizar_numero(54)
print(resultado['cuadrado'])  
print(resultado['cubo'])     
print(resultado['mitad'])    


#FUNCIONES QUE TRABAJAN CON LISTAS......................
#Ejemplo 1: Sumar todos los elementos de una lista
def sumar_lista(numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total
print(sumar_lista([1,2,3,4,5,6,7,8,9]))
print(sumar_lista([21,23,43,21,34,55,43]))

#Ejemplo 2: Encontrar el número más grande
def encontrar_mayor(numeros):
    mayor = numeros[0]
    for numero in numeros:
        if numero > mayor:
            mayor = numero
        return mayor
print(encontrar_mayor([5, 8, 2, 10, 3]))  
print(encontrar_mayor([-5, -2, -10]))

#Ejemplo 3: Filtrar Números Pares
def filtrar_pares(numeros):
    pares = []
    for numero in numeros:
        pares.append(numero)
        return pares
print(filtrar_pares[1,2,3,4,5,6])


#FUNCIONES QUE USAN OTRAS FUNCIONES
#Ejemplo 1: Aplicar operación a una lista
def aplicar_operacion(numeros, operacion):
    resultado = []
    for numero in numeros:
        resultado.append(operacion(numero))
    return resultado

def duplicar(x):
    return x * 2

def elevar_cuadrado(x):
    return x ** 2

# Usar las funciones
numeros = [1, 2, 3, 4, 5]
print(aplicar_operacion(numeros, duplicar))       # [2, 4, 6, 8, 10]
print(aplicar_operacion(numeros, elevar_cuadrado)) # [1, 4, 9, 16, 25]

#Ejemplo 2: Función que devuelven otra función
def crear_multiplicador(factor):
    def multiplicar(numero):
        return numero * factor
    return multiplicar

duplicar = crear_multiplicador(2)
triplicar = crear_multiplicador(3)

print(duplicar(5))  # 10
print(triplicar(5)) # 15 

"""REPASAR LAS FUNCIONES CON ARCHIVOS"""

#FUNCIONES CON ARCHIVOS (BASICAS)
#Ejemplo 1: Guardar texto en un archivo
def guardar_texto(nombre_archivo, contenido):
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        archivo.write(contenido)
    print(f"✅ Archivo {nombre_archivo} guardado")

guardar_texto("mensaje.txt", "Hola, este es mi primer archivo")

#Ejemplo 2: Leer texto de un archivo
def leer_texto(nombre_archivo):
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            return archivo.read()
    except FileNotFoundError:
        return "❌ Archivo no encontrado"

print(leer_texto("mensaje.txt"))  # Hola, este es mi primer archivo


"""Repasar Json """
#FUNCIONES CON JSON (BÁSICO)
#Ejemplo 1: Guardar lista en Json
import json

def guardar_json(datos, archivo="datos.json"):
    with open(archivo, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)
    print(f"✅ Datos guardados en {archivo}")

tareas = ["Aprender Python", "Estudiar funciones", "Hacer ejercicios"]
guardar_json(tareas)

#Ejemplo 2: Guaradar varias lineas
def guardar_varias_lineas(nombre_archivo, lineas):
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        for linea in lineas:
            archivo.write(linea + "\n")
    print(f"✅ {len(lineas)} líneas guardadas en '{nombre_archivo}'")

# USAR LA FUNCIÓN
lineas = [
    "Primera línea",
    "Segunda línea",
    "Tercera línea",
    "Cuarta línea",
    "Quinta línea",
    "Sexta línea",
    "Septima línea",
    "Octava línea",
    "Novena línea",
    "Decima línea",
    "Undecima línea"
]
guardar_varias_lineas("mi_archivo.txt", lineas)

#Ejemplo 3: Guardar información de una persona
def guardar_persona(nombre_archivo, nombre, edad, ciudad):
    contenido = f"Nombre: {nombre} \nEdad: {edad} \nCiudad: {ciudad}"
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        archivo.write(contenido)
    print(f"✅ Datos de {nombre} guardados en '{nombre_archivo}'")

guardar_persona("persona.txt", "Ana", 25, "Bogotá")

#Ejemplo 4: Cargar desde Json
def cargar_json(archivo="datos.json"):
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print("❌ Archivo no encontrado")
        return []

tareas = cargar_json("datos.json")
print(tareas)  # ["Aprender Python", "Estudiar funciones", "Hacer ejercicios"]