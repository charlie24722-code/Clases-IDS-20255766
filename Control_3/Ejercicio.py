agente = "encargado"
platillo = []
precios = []

sistema_encendido = True
ingreso = ""

while agente.casefold() != ingreso.casefold():
    ingreso = input("Favor ingrese el nombre del agente: ")
    if agente.casefold() != ingreso.casefold():
        print("agente no registrado")
        print(f"{ingreso}")

while sistema_encendido:
    opcion = int(input("1. Creación de platillos, 2. Consulta de platillos y precios, 3. Colocar un pedido, 4. Salir"))
    if opcion == 1:
        platillo.append(input("Ingrese el nombre del platillo a crear: ").lower())
        precios.append(float(input("Ingrese el precio del platillo a crear: ")))
    elif opcion == 2:
        if len(platillo) == 0:
            print("Actualmente no hay platillos ingresados")
        else: 
            for consulta in range(len(platillo)):
                    print(f"{platillo[consulta].capitalize()}: ${precios[consulta]:.2f}")
    elif opcion == 3:
        platillo_elegido = input("Indique el nombre del platillo para su orden: ")
        if platillo_elegido.lower() in platillo:
            indice = platillo.index(platillo_elegido.lower())
            print(f"Usted ha elegido {platillo[indice]} con un precio de ${precios[indice]}")
        elif platillo_elegido.lower() not in platillo:
            print("Este platillo no existe")
    else:
        if opcion == 4:
            sistema_encendido = False     
        break       
            