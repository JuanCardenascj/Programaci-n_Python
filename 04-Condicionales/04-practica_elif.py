#PRACTICA ELIF (CONDICIONALES)

emanuel = 1200

if emanuel > 1200:
    print("Cuentas con los estudiantes suficientes para el regreso a clases")
elif emanuel < 1200:
    print("Aún estas a tiempo para lograr mas estudiantes")
elif emanuel == 1200:
    print("Estas en el tope limite")


cuentas_mensuales = 1200000
gastos_mensuales = 20000
tope_gastos = 40000

if gastos_mensuales > tope_gastos:
    print("Tus gastos están sobrepasando tu tope")
elif gastos_mensuales < tope_gastos:
    print("Tus gastos están dentro del límite")
else:
    print("Estás gastando exactamente el tope")


arcane = 900000

if arcane > 90000:
    print("Estás haciendo demasiado daño")
elif arcane == 90000:
    print("Estás haciendo daño sostenido!")
elif arcane >= 70000:
    print("Estás en el límite máximo, aún puedes hacer más daño")
else:
    print("Aún te falta mucho daño, vas a perder la partida")
