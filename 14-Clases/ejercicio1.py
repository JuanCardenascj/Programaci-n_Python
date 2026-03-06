""" Ejercicios Propuestos..!!
1. Elaborar el diagrama de clases y la codificación del constructor, los métodos set y get; para cada uno de los siguientes enunciados:

   a. Se requiere modelar la información de un libro conformado, por el titulo, editorial, número de páginas y el autor.
   b. Modelar la información correspondiente al teléfono, conformada por la referencia, costo, marca, modelo.

Construir la clase Docente, la cual estará integrada por los siguientes atributos:

    Visibilidad        Nombre atributo      Tipo
Private             Nombre                 String
Private             Documento              Long
Private             Teléfono               String
Private             Email                  String
  
1. Crear uno o más constructores para la clase
2. Crear los métodos get y set para los distintos atributos de la clase
3. Elaborar una clase que implemente los métodos para obtener, la raíz cuadrada, el logaritmo en base 10, logatirmo en base e.
4. Diseñar una clase que provea los métodos para las funciones trigonométricas de seno, coseno y tangente; expresados en radiantes.
"""

class Libro:

    def __init__(self, titulo, editorial, paginas, autor):
        self.__titulo = titulo
        self.__editorial = editorial
        self.__paginas = paginas
        self.__autor = autor

    # getters
    def get_titulo(self):
        return self.__titulo

    def get_editorial(self):
        return self.__editorial

    def get_paginas(self):
        return self.__paginas

    def get_autor(self):
        return self.__autor

    # setters
    def set_titulo(self, titulo):
        self.__titulo = titulo

    def set_editorial(self, editorial):
        self.__editorial = editorial

    def set_paginas(self, paginas):
        self.__paginas = paginas

    def set_autor(self, autor):
        self.__autor = autor

class Telefono:

    def __init__(self, referencia, costo, marca, modelo):
        self.__referencia = referencia
        self.__costo = costo
        self.__marca = marca
        self.__modelo = modelo

    # getters
    def get_referencia(self):
        return self.__referencia

    def get_costo(self):
        return self.__costo

    def get_marca(self):
        return self.__marca

    def get_modelo(self):
        return self.__modelo

    # setters
    def set_referencia(self, referencia):
        self.__referencia = referencia

    def set_costo(self, costo):
        self.__costo = costo

    def set_marca(self, marca):
        self.__marca = marca

    def set_modelo(self, modelo):
        self.__modelo = modelo

class Docente:

    def __init__(self, nombre, documento, telefono, email):
        self.__nombre = nombre
        self.__documento = documento
        self.__telefono = telefono
        self.__email = email

    # getters
    def get_nombre(self):
        return self.__nombre

    def get_documento(self):
        return self.__documento

    def get_telefono(self):
        return self.__telefono

    def get_email(self):
        return self.__email

    # setters
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_documento(self, documento):
        self.__documento = documento

    def set_telefono(self, telefono):
        self.__telefono = telefono

    def set_email(self, email):
        self.__email = email

import math

class FuncionesMatematicas:

    def __init__(self, x):
        self.x = x

    def raiz_cuadrada(self):
        return math.sqrt(self.x)

    def log_base10(self):
        return math.log10(self.x)

    def log_base_e(self):
        return math.log(self.x)
    
import math

class FuncionesTrigonometricas:

    def __init__(self, x):
        self.x = x

    def seno(self):
        return math.sin(self.x)

    def coseno(self):
        return math.cos(self.x)

    def tangente(self):
        return math.tan(self.x)
    


docente1 = Docente("Carlos Perez", 12345678, "3001234567", "carlos@email.com")

print(docente1.get_nombre())
print(docente1.get_email())

mat = FuncionesMatematicas(100)
print(mat.raiz_cuadrada())
print(mat.log_base10())

trig = FuncionesTrigonometricas(3.14)
print(trig.seno())