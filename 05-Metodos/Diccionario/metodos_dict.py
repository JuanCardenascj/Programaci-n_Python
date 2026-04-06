"""Estructura de Datos:
1. Hash Table - Almacenamiento de valores
2. Clave - Valor"""

#Declaración Basica del Diccionario
mi_diccionario = {
    'Edward' : [1.4, 4.3, 5.0],
    'Carla' : [4.4, 5.0, 5.0],
    'Jonas' : [0.0, 3.4, 3.0]
}

#Declaración con el Método Dict
mi_diccionario2 = dict(Edward = [1.4, 4.3, 5.0],
                       Carla = [4.4, 5.0, 5.0],
                       Jonas = [0.0, 3.4, 3.0])

#Declaración con el diccionario vacio
mi_diccionario3 = dict()
mi_diccionario3['Edwar'] = [1.4, 4.3, 5.0]
mi_diccionario3['Carla']= [4.4, 5.0, 5.0]
mi_diccionario3['Jonas'] = [0.0, 3.4, 3.0]

#Keys
print(mi_diccionario.keys())

#Values
print(mi_diccionario2.values())

#Both
print(mi_diccionario3.items())