"""
Crea una función que:

Reciba tres números
Devuelva un diccionario con: suma, promedio, mayor y menor
"""
def estadisticas(a, b, c):
    return {
        'suma': a + b + c,
        'promedio': (a + b + c) / 3,
        'mayor': max(a, b, c),
        'menor': min(a, b, c)
    }
resultado = estadisticas(10, 20, 30)
print(resultado['suma'])      
print(resultado['promedio'])  
print(resultado['mayor'])     
print(resultado['menor'])     