# Vamos a jugar un juego
aprobacion =  True

while aprobacion:
    eleccion = input("Quieres seguir jugando (Y/N)")
    if eleccion[0].lower() == "n":
        aprobacion = False
    elif eleccion[0].lower() == "y":
        print("Me alegra que quieras seguir jugando!")
    else:
        print("La opcion elegida no es valida. ")       