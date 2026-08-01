import pandas as pd
import matplotlib.pyplot as plt
import os
import json

# ============================================
# 1. FUNCIONES (Nivel Intermedio)
# ============================================
def cargar_datos(ruta_archivo):
    """Carga datos desde un archivo CSV"""
    return pd.read_csv(ruta_archivo)

def calcular_top_productos(ventas, n=5):
    """Calcula los n productos más vendidos"""
    return ventas.groupby('producto')['cantidad'].sum().sort_values(ascending=False).head(n)

def guardar_resultados(resultados, nombre_archivo):
    """Guarda resultados en un archivo JSON"""
    with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
        json.dump(resultados, archivo, indent=4, ensure_ascii=False)

def crear_grafico_barras(datos, titulo, xlabel, ylabel, archivo_salida=None):
    """Crea un gráfico de barras y opcionalmente lo guarda"""
    plt.figure(figsize=(10, 6))
    plt.bar(datos.index, datos.values, color='skyblue')
    plt.title(titulo)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(axis='y', alpha=0.3)
    
    if archivo_salida:
        plt.savefig(archivo_salida, dpi=300)
        print(f"📊 Gráfico guardado como {archivo_salida}")
    
    plt.show()

# ============================================
# 2. CARGA DE DATOS (Archivos)
# ============================================
# Obtener la ruta correcta
carpeta_script = os.path.dirname(os.path.abspath(__file__))
ruta_csv = os.path.join(carpeta_script, "ventas.csv")

# Cargar datos usando la función
ventas = cargar_datos(ruta_csv)

# Crear columnas calculadas
ventas['total'] = ventas['cantidad'] * ventas['precio_unitario']
ventas['fecha'] = pd.to_datetime(ventas['fecha'])
ventas['mes'] = ventas['fecha'].dt.month

# ============================================
# 3. ANÁLISIS (Pandas)
# ============================================
print("=" * 60)
print("📊 ANÁLISIS DE VENTAS COMPLETO")
print("=" * 60)

# Calcular top productos usando la función
top_5 = calcular_top_productos(ventas)

print("\n🏆 TOP 5 PRODUCTOS MÁS VENDIDOS:")
for i, (producto, cantidad) in enumerate(top_5.items(), 1):
    print(f"   {i}. {producto}: {cantidad} unidades")

# Análisis por mes
ventas_por_mes = ventas.groupby('mes').agg({
    'cantidad': 'sum',
    'total': 'sum'
}).reset_index()

print("\n📈 VENTAS POR MES:")
meses = ['Enero', 'Febrero', 'Marzo']
for _, row in ventas_por_mes.iterrows():
    print(f"   {meses[row['mes']-1]}: {row['cantidad']} unidades - ${row['total']:,.0f}")

# ============================================
# 4. GRÁFICOS (Matplotlib)
# ============================================
# Gráfico 1: Top productos
crear_grafico_barras(
    top_5,
    'Top 5 Productos Más Vendidos',
    'Producto',
    'Unidades Vendidas',
    'top_productos.png'
)

# Gráfico 2: Ventas por mes
ventas_por_mes_dict = ventas_por_mes.set_index('mes')['total']
ventas_por_mes_dict.index = ['Enero', 'Febrero', 'Marzo']

crear_grafico_barras(
    ventas_por_mes_dict,
    'Ventas Totales por Mes',
    'Mes',
    'Ingresos ($)',
    'ventas_por_mes.png'
)

# ============================================
# 5. GUARDAR RESULTADOS (JSON)
# ============================================
resultados = {
    'top_productos': dict(top_5),
    'ventas_por_mes': ventas_por_mes.to_dict(orient='records')
}

guardar_resultados(resultados, 'resultados_analisis.json')
print("\n💾 Resultados guardados en 'resultados_analisis.json'")

print("\n✅ ANÁLISIS COMPLETADO CON ÉXITO")