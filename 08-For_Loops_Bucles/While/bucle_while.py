"""While --> Utilizada para repetir una tarea N cantidad de veces de acuerdo a una condición, mientras sea verdadera"""

nombre = ""
correo = ""
mensaje = ""

condicion_salida = "CONTINUE..!"

#Definición del ciclo while...

while condicion_salida == "CONTINUE..!":
    nombre = input("Por favor Digite su nombre ... ")
    correo = input("Por favor Digite su correo.... ")
    mensaje = input("Por favor Digite su mensaje a enviar ... ")

    print(f"""
Mensaje enviado a {nombre} con el correo de {correo} y el mensaje enviado es: {mensaje}
          """)
    condicion_salida = input("En caso de querer continuar con el programa escriba CONTINUE: ")