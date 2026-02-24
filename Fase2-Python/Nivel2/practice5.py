"""
🎯 Ejercicio para ti (nivel intermedio)

Tienes:

usuarios_registrados = {"Juan", "Maria", "Pedro", "Ana"}
usuarios_con_solicitud = {"Maria", "Pedro"}

¿Quiénes NO han hecho solicitud?

¿Quiénes sí han hecho solicitud?

¿Existe algún usuario con solicitud que no esté registrado?

Escríbelo tú primero.
Luego lo revisamos paso a paso.

Estamos entrando en pensamiento estructural.
Esto ya no es solo Python.
Es modelado lógico.

¿Listo? 😎
"""

usuarios_registrados = {"Juan", "Maria", "Pedro", "Ana"}
usuarios_con_solicitud = {"Maria", "Pedro"}

#Quienes no han hecho solicitud
usuarios_sin_solicitud = usuarios_registrados - usuarios_con_solicitud
print(usuarios_sin_solicitud)

#Quienes si han hecho solicitud
print(usuarios_con_solicitud)

#Si se quiere asegurar de que estén registrados
usuarios_validos = usuarios_registrados & usuarios_con_solicitud
print(usuarios_validos)

#Existe algun usuario no registrado
no_registrados = usuarios_con_solicitud - usuarios_registrados
print(no_registrados)
