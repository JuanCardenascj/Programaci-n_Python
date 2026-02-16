"""Otra condicion"""

ingreso_mensual = 81000
gasto_mensual = 80000

#If anidados y Else if (elif)

if ingreso_mensual > 10000:
    if ingreso_mensual - gasto_mensual < 0:
        print("Ahora si  estas bien")
    elif ingreso_mensual - gasto_mensual > 3000:
        print("bien pam estasbien")
    else: 
        print("ya para, estas gastando mucho dinero")

elif ingreso_mensual > 1000:
    print("Estas bien en latinoamerica")
else: 
    print("Sos pobre")
