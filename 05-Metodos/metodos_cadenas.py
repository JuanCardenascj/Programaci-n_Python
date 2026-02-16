"""Metodos - Debe ser ejecutados con el (.)"""

cadena1 = "Bienvenidos a tu canal"
cadena2 = "A que opción deseas acceder"

#Para convertir a mayusculas
resultado = cadena1.upper()
print(resultado)

#Para convertir a minusculas
resultado2 = cadena2.lower()
print(resultado2)

#Primera letra en mayuscula
primer_letra_mayuscu = cadena1.capitalize()
print(primer_letra_mayuscu)

#Para buscar una cadena en otra cadena - Si no hay coindicidencias devuelven -1
busqueda_find = cadena2.find("o") #La "o" se encuentra en la posición 6
print(busqueda_find)

#Buscamos una cadena dentro de otra con INDEX - Si no hay coincidencias lanza una excepción
busqueda_index = cadena1.index("p")
print(busqueda_index)

#Si es numerico devolvemos True, sino devolvemos False
es_numerico = cadena1.isnumeric()
print(es_numerico)

#Si es alfanumerico devolvemos true, sino devolvemos false
es_alfanumerico = cadena2.isalpha("a")
print(es_alfanumerico)

#Separar cadenas con la cadena que se le pase
cadena_separada = cadena1.split(",")
print(cadena_separada)