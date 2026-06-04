"""Es un Set que no se puede modificar
1. Es inmutable
2. No son tan utilizados
3. No se puede modificar
4. No requiere espacio adicional para los cambios"""

frutas = {'Manzana',
          'Banano', 
          'Pera', 
          'Uva'}

#Declaración con función
mi_frozenset = frozenset(frutas)
print(mi_frozenset)