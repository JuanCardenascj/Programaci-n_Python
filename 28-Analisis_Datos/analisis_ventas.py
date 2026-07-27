import pandas as pd
import os

# 1. CARGAR DATOS
carpeta_actual = os.path.dirname(os.path.abspath(__file__))
ruta_completa = os.path.join(carpeta_actual, "ventas.csv")
ventas = pd.read_csv(ruta_completa)

# 2. CREAR COLUMNA DE TOTAL
ventas['total'] = ventas['cantidad'] * ventas['precio_unitario']

# 3. MOSTRAR INFORMACIÓN BÁSICA
print("=" * 60)
print("📊 ANÁLISIS DE VENTAS - INFORME EJECUTIVO")
print("=" * 60)

print("\n1️⃣  DATOS BÁSICOS")
print(f"   - Total de ventas registradas: {len(ventas)}")
print(f"   - Período: {ventas['fecha'].min()} hasta {ventas['fecha'].max()}")
print(f"   - Total de productos diferentes: {ventas['producto'].nunique()}")
print(f"   - Categorías: {', '.join(ventas['categoria'].unique())}")

# 4. TOP 5 PRODUCTOS MÁS VENDIDOS (por cantidad)
print("\n2️⃣  TOP 5 PRODUCTOS MÁS VENDIDOS (por unidades)")
top_cantidad = ventas.groupby('producto')['cantidad'].sum().sort_values(ascending=False).head(5)
for i, (producto, cantidad) in enumerate(top_cantidad.items(), 1):
    print(f"   {i}. {producto}: {cantidad} unidades")

# 5. TOP 5 PRODUCTOS QUE MÁS INGRESOS GENERAN
print("\n3️⃣  TOP 5 PRODUCTOS QUE MÁS FACTURAN")
top_ingresos = ventas.groupby('producto')['total'].sum().sort_values(ascending=False).head(5)
for i, (producto, total) in enumerate(top_ingresos.items(), 1):
    print(f"   {i}. {producto}: ${total:,.0f}")

# 6. VENTAS POR CATEGORÍA
print("\n4️⃣  VENTAS POR CATEGORÍA")
ventas_categoria = ventas.groupby('categoria')[['cantidad', 'total']].sum()
for categoria, row in ventas_categoria.iterrows():
    print(f"   📌 {categoria}")
    print(f"      - Unidades vendidas: {row['cantidad']}")
    print(f"      - Ingresos totales: ${row['total']:,.0f}")

# 7. VENTAS POR MES
print("\n5️⃣  VENTAS POR MES")
ventas['mes'] = pd.to_datetime(ventas['fecha']).dt.month
ventas_mes = ventas.groupby('mes')[['cantidad', 'total']].sum()
meses = {1: 'Enero', 2: 'Febrero', 3: 'Marzo'}
for mes, row in ventas_mes.iterrows():
    print(f"   📆 {meses[mes]}: {row['cantidad']} unidades - ${row['total']:,.0f}")

# 8. ESTADÍSTICAS DE PRECIOS
print("\n6️⃣  ESTADÍSTICAS DE PRECIOS")
print(f"   💰 Producto más caro: ${ventas['precio_unitario'].max():,.0f}")
print(f"   💰 Producto más barato: ${ventas['precio_unitario'].min():,.0f}")
print(f"   💰 Precio promedio: ${ventas['precio_unitario'].mean():,.0f}")

# 9. PRODUCTO ESTRELLA (mayor cantidad total vendida)
producto_estrella = ventas.groupby('producto')['cantidad'].sum().idxmax()
cantidad_estrella = ventas.groupby('producto')['cantidad'].sum().max()
print(f"\n⭐ PRODUCTO ESTRELLA: {producto_estrella} con {cantidad_estrella} unidades vendidas")

print("\n" + "=" * 60)
print("📋 FIN DEL INFORME")
print("=" * 60)