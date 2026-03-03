"""
Un usuario tiene:

nombre

puntos

estado activo

lista de solicitudes

métodos para sumar puntos

método para desactivar

método para crear solicitud

método para mostrar información

Un diccionario solo guarda datos.

Un set solo guarda datos únicos.

Pero un usuario real en un sistema no es solo datos.

Es:

🔥 Datos + Comportamiento

Y eso en programación se llama:

🧠 Objeto
"""

class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.puntos = 0
        self.activo = True
        self.solicitudes = []

    def sumar_puntos(self, cantidad):
        self.puntos += cantidad

    def desactivar(self):
        self.activo = False

u1 = Usuario("Juan")
u1.sumar_puntos(10)

# .

# 🎯 ¿Por qué es mejor?

# Porque:

# Encapsula comportamiento

# Controla el estado

# Reduce errores

# Organiza el sistema

# Escala mejor

# Es lo que se usa en backend real

# Y ahora viene lo interesante…

# Tú ya estabas listo para esto.
# Por eso te hice tantas preguntas sobre mutabilidad antes.

class Usuario:
    puntos = 0   # variable de clase

    def __init__(self, nombre):
        self.nombre = nombre

u1 = Usuario("Ana")
u2 = Usuario("Pedro")

u1.puntos += 10

"""
🧠 Entonces regla de oro:

Variables dentro de __init__ con self. → son de instancia.

Variables fuera del __init__ → son de clase.

Las de clase se comparten… hasta que una instancia las sobrescribe.
"""

# Y ahora viene la pregunta que separa nivel medio de nivel sólido:

# ¿En tu sistema de usuarios (como el que estás desarrollando),
# los puntos deberían ser variable de clase o variable de instancia?

# Respóndeme como arquitecto, no como estudiante. 💪

#De instancia, porque cada uno tiene su propio estado, no deben afectar a otros usuarios, representan información individual persistente, modelan una entidad real.

#Si fueran de clase, todos compartirían el mismo contador base, podría tener comportamientos impredecibles, sería un diseño incorrecto del dominio.!