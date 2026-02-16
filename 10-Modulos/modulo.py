#Importando un modulo y asignandole el nombre "m_saludar"
#import modulo_saludar as m_saludar

#Desde ese modulo, importamos dos funciones
from modulo_saludar import saludar,saludar_raro

#Creamos las variables con los dos saludos
saludo = saludar("David")
saludo_raro = saludar_raro("Frank")

#Mostramos los resultados
print(saludo)
print(saludar_raro)