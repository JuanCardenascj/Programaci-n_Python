#Dos maneras de importar!
import Aritmeticas.operaciones_basicas as ob
from Aritmeticas.operaciones_avanzadas import (multiplicar, dividir)

resultado = ob.sumar(23, 51)
print(resultado)

resultado = ob.restar(23, 51)
print(resultado)

resultado = multiplicar(23, 51)
print(resultado)

resultado = dividir(23, 51)
print(resultado)