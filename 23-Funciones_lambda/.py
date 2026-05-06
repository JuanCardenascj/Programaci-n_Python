"""Se denominan funciones anonimas --> Caracterizadas por ser bastante sencillas, por tener un unico nombre!

Funcion: Pueden agrupar un grupo de funciones y pueden ser ejecutadas a lo largo del codigo """

lista_estudiantes = [('David', 5.0),
                     ('Luis', 4.0),
                     ('Kenia', 4.5),
                     ('Daniel', 3.0),
                     ('Juan0', 3.5)]

#Se crea la función anonima!
lista_ordenada = sorted(lista_estudiantes, key=lambda x:x[1], reverse=True)
print(lista_ordenada)