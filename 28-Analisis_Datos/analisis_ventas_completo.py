import pandas as pd
import matplotlib.pyplot as plt #Librería para hacer graficos
import os  # <--- NUEVA LIBRERÍA PARA MANEJAR RUTAS

# Cargar datos
ventas = pd.read_csv("ventas.csv")

# Ver los datos
print("=== DATOS DE VENTAS ===")
print(ventas.head())
print("\n")

# Crear columna de total
ventas['total'] = ventas['cantidad'] * ventas['precio_unitario']

# Convertir fecha a datetime
ventas['fecha'] = pd.to_datetime(ventas['fecha'])
ventas['mes'] = ventas['fecha'].dt.month
ventas['dia'] = ventas['fecha'].dt.day