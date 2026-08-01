import matplotlib.pyplot as plt

# 1. Datos Laborales
dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']
materias = [2, 3, 1, 4, 2, 0, 1]

# 2. Crear el gráfico
plt.figure(figsize=(10, 6))           # Tamaño del gráfico
plt.bar(dias, materias, color=['blue'])   # Barras colores
plt.title('Materias Actuales')        # Título
plt.xlabel('Día de la semana')        # Etiqueta eje X
plt.ylabel('Materias')         # Etiqueta eje Y
plt.grid(axis='y', alpha=0.3)         # Líneas de ayuda

# 3. Mostrar
plt.show()