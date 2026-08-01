import pandas as pd
import matplotlib.pyplot as plt
import os

# ============================================
# CONFIGURACIÓN DE RUTAS
# ============================================
carpeta_script = os.path.dirname(os.path.abspath(__file__))
ruta_csv = os.path.join(carpeta_script, "ventas.csv")

print(f"📂 Buscando archivo en: {ruta_csv}")
print("=" * 60)

# Verificar si el archivo existe
if not os.path.exists(ruta_csv):
    print(f"❌ ERROR: No se encontró el archivo {ruta_csv}")
    print("📌 Asegúrate de que el archivo ventas.csv esté en la misma carpeta que este script")
    exit()

print("✅ Archivo encontrado, cargando datos...\n")

# ============================================
# CARGAR DATOS
# ============================================
ventas = pd.read_csv(ruta_csv)

# Crear columnas
ventas['total'] = ventas['cantidad'] * ventas['precio_unitario']
ventas['fecha'] = pd.to_datetime(ventas['fecha'])
ventas['mes'] = ventas['fecha'].dt.month

print("=== DATOS CARGADOS CORRECTAMENTE ===")
print(ventas.head())
print("\n")

# ============================================
# ANÁLISIS POR MES
# ============================================
ventas_por_mes = ventas.groupby('mes').agg({
    'cantidad': 'sum',
    'total': 'sum'
}).reset_index()

print("=" * 60)
print("📊 ANÁLISIS DE VENTAS POR MES")
print("=" * 60)

meses_nombres = ['Enero', 'Febrero', 'Marzo']
for _, row in ventas_por_mes.iterrows():
    mes_nombre = meses_nombres[row['mes'] - 1]
    print(f"   {mes_nombre}: {row['cantidad']} unidades - ${row['total']:,.0f}")

# ============================================
# GRÁFICO 1: VENTAS POR MES
# ============================================
print("\n📊 CREANDO GRÁFICO DE VENTAS POR MES...")

#Tamaño en pulgadas (Ancho y Alto)
plt.figure(figsize=(10, 6))
#Dibujar Barras
plt.bar(meses_nombres, ventas_por_mes['total'], color=['#3498db', '#2ecc71', '#e74c3c'])
#Títulos
plt.title('Ventas Totales por Mes', fontsize=16) #Título del gráfico
plt.xlabel('Mes', fontsize=12) #Etiqueta del eje x
plt.ylabel('Ingresos ($)', fontsize=12) #Etiqueta del eje y
plt.grid(axis='y', alpha=0.3)

for i, v in enumerate(ventas_por_mes['total']):
    plt.text(i, v + 500000, f'${v:,.0f}', ha='center', fontsize=10)

plt.tight_layout()
plt.show() #Mostrar el gráfico

# ============================================
# GRÁFICO 2: DISTRIBUCIÓN POR CATEGORÍA
# ============================================
print("\n📊 CREANDO GRÁFICO DE DISTRIBUCIÓN POR CATEGORÍA...")

ventas_categoria = ventas.groupby('categoria')['total'].sum()

plt.figure(figsize=(8, 8))
plt.pie(ventas_categoria, labels=ventas_categoria.index, autopct='%1.1f%%',
        colors=['#3498db', '#e74c3c'], startangle=90, explode=(0.05, 0.05))
plt.title('Distribución de Ventas por Categoría', fontsize=16)
plt.show()

# ============================================
# GRÁFICO 3: TOP PRODUCTOS
# ============================================
print("\n📊 CREANDO GRÁFICO DE TOP PRODUCTOS...")

top_productos = ventas.groupby('producto')['cantidad'].sum().sort_values(ascending=False).head(5)

plt.figure(figsize=(10, 6))
colors = ['#3498db', '#2ecc71', '#f39c12', '#e74c3c', '#9b59b6']
plt.bar(top_productos.index, top_productos.values, color=colors)
plt.title('Top 5 Productos Más Vendidos', fontsize=16)
plt.xlabel('Producto', fontsize=12)
plt.ylabel('Unidades Vendidas', fontsize=12)
plt.grid(axis='y', alpha=0.3)

for i, v in enumerate(top_productos.values):
    plt.text(i, v + 0.5, str(v), ha='center', fontsize=10)

plt.tight_layout()
plt.show()

print("\n✅ ANÁLISIS COMPLETADO CON ÉXITO")