import pandas as pd #PD es un alias

datos1 = {
    "nombre" : ["Ana", "Luis", "Carlos", "Marta"],
    "edad" : [25, 30, 28, 35],
    "ciudad" : ["Bogota", "Medellin", "Cali", "Arauca"],
    "salario" : [250000, 325000, 6541235, 4000000]
}

#Convertir en un dataframe 
# --> pd.DataFrame es el constructor que crea una tabla
# --> df es el nombre de nuestra tabla (DataFrame)
df1 = pd.DataFrame(datos1)

#Para mostrar el DataFrame
print("== DATOS DE EMPLEADOS ===")
print(df1)

#Explorar el DataFrame

print("\n=== INFORMACIÓN GENERAL ===")
print(df1.info())

print("\n=== ESTADÍSTICAS BÁSICAS ===")
print(df1.describe())

print("\n=== PRIMERAS 2 FILAS ===")
print(df1.head(2))

print("\n=== ÚLTIMAS 2 FILAS ===")
print(df1.tail(2))

#Filtrar Datos
print("\n=== EMPLEADOS DE BOGOTÁ ===")
bogotanos = df1[df1["ciudad"] == "Bogota"]
print(bogotanos)

#Filtrar por Salario
print("\n=== EMPLEADOS QUE GANAN > 3,000,000 ===")
empleados_ricos = df1[df1["salario"] > 3000000]
print(empleados_ricos)

#Filtar por ciudad y salario
print("\n=== EMPLEADOS DE BOGOTÁ CON SALARIO > 3,000,000 ===")
filtro = (df1["ciudad"] == "Bogotá") & (df1["salario"] > 3000000)
bogotanos_ricos = df1[filtro]
print(bogotanos_ricos)

#Agrupar y Sumar
#--> df.groupby("ciudad") → Agrupa por ciudad (Bogotá, Medellín, Cali)
print("\n=== SALARIO TOTAL POR CIUDAD ===")
salario_por_ciudad = df1.groupby("ciudad")["salario"].sum()
print(salario_por_ciudad)

#Crear Nuevas Columnas
# --> df["salario_anual"] → Crea una nueva columna
# --> = df["salario"] * 12 → Multiplica el salario mensual por 12
# --> df[["nombre", "salario", "salario_anual"]] → Muestra solo esas columnas
print("\n=== SALARIO ANUAL ===")
df1["salario_anual"] = df1["salario"] * 12
print(df1[["nombre", "salario", "salario_anual"]])

#Ordenar Los Datos
print("\n=== EMPLEADOS ORDENADOS POR SALARIO (MAYOR A MENOR) ===")
ordenados = df1.sort_values("salario", ascending=False)
print(ordenados[["nombre", "salario", "ciudad"]])

print("\n")

"""Ahora Practicando Analisis De Datos Con Información de Familiares...."""
#Datos con Familiares

familia = {
    "nombre" : ["Silvia Juliana", "Leidy Karime", "Carmen Zoraida", "Jorge Andres", "Erick Gustavo", "Jorge Alberto", "Alan Torres", "Ethan Elian", "Adrian Stevan", "Juan David", "Ruby Carlota", "Marta Stella", "Victor Herman", "Cesar Ivan", "Ernestina Mogollon", "Juan Tellez", "Cesar David", "Pacho Lobo"],
    "edad" : [30, 40, 50, 25, 20, 67, 14, 7, 3, 30, 50, 55, 60, 50, 85, 20, 20, 13],
    "ciudad" : ["Arauca", "Arauca", "Arauca", "Arauca", "Arauca", "Arauca", "Arauca", "Arauca", "Arauca", "Arauca", "Bucaramanga", "Bucaramanga", "Bucaramanga", "Bucaramanga", "Bucaramanga", "Bucaramanga", "Bucaramanga", "Bucaramanga"],
    "empleado" : ["Si", "Ama de casa", "Ama de casa", "No", "Estudiante", "Pensionado", "Estudiante", "Estudiante", "Formación", "Estudiante - Desempleado", "Pensionada", "Pensionada", "Si", "Si", "Pensionada", "Estudiante", "Estudiante", "Animal"]
}

df2 = pd.DataFrame(familia)

print("===== Datos de la Familia Cárdenas_Vega_Macualo_Torres_Duarte_Garcia")
print(df2)

#Explorar el DataFrame

print("\n=== INFORMACIÓN GENERAL ===")
print(df2.info())

print("\n=== ESTADÍSTICAS BÁSICAS ===")
print(df2.describe())

print("\n=== PRIMERAS 2 FILAS ===")
print(df2.head(2))

print("\n=== ÚLTIMAS 2 FILAS ===")
print(df2.tail(2))

#Filtrar Datos Empleo
print("\n=== FAMILIARES DE ARAUCA  ===")
filtro2 = (df2["ciudad"] == "Arauca") & (df2["empleado"] == "Si")
araucanos = df2[filtro2]
print(araucanos)

#Filtrar Datos Ama de casa
print("\n=== FAMILIARES AMAS DE CASA ===")
ama_casa = df2[df2["empleado"] == "Ama de casa"]
print(ama_casa)

#Filtrar Datos Por Edad
print("\n=== FAMILIARES MENOR DE EDAD ===")
filtro3 = (df2["edad"] <= 17) & (df2["ciudad"] == "Arauca")
menores = df2[filtro3]
print(menores)

#Filtrar Datos por Edad
print("\n=== FAMILIARES MAYORES DE EDAD ===")
mayores = df2[df2["edad"] >= 18]
print(mayores)

#Filtrar Datos Por Cantidad de Familiares
print("\n=== CANTIDAD DE FAMILIARES POR CIUDAD ===")
conteo_por_ciudad = df2.groupby("ciudad")["nombre"].count()
print(conteo_por_ciudad)