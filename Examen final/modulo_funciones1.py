from modulo_datos import clientes, sabores, pedidos
# funcion para registrar_cliente
def registrar_cliente():
    """Esta función permite registrar un cliente"""
    try:
       while True:
# Variables para el diccionario de clientes
        nombre = input("Digite su nombre: ").lower()
        correo = input("Digite su correo electrónico: ").lower()

# Condiciones para validar los datos ingresados
        if len(nombre) < 2:
            print("El nombre debe de contener 2 caracteres o más")
        elif not correo:
            print("El correo no puede estar vacio")    
        elif correo in clientes:
            print("El correo ya existe en el sistema")
        else:
            clientes[correo] = nombre
            print("Cliente registrado exitosamente")
            break   
    except Exception as e:
       print(f"Lo sentimos, la entrada no fue valida: {e}") 
   
# definimos la función registrar pedido
def registrar_pedidos():
    """Esta función permite registrar un pedido"""
    try:
        while True:
            sol_correo = input("Digite su correo electrónico (o escriba 'salir' si desea regresar al menu principal): ").lower()
            if sol_correo == "salir":
                return
            elif sol_correo in clientes: 
                print(sabores)
                sabor_sel = input("Seleccione el sabor que desea (ingrese la primera letra del sabor): ").lower()
                # para mostrar el sabor seleccionado utilizando del diario
                if sabor_sel == "c":
                    for sabor in sabores:
                        if sabor == "CH":
                            sabor_sel = sabores[sabor]
                            print(sabor_sel)   
                    break
                elif sabor_sel == "v":
                    for sabor in sabores:
                        if sabor == "VA":
                            sabor_sel = sabores[sabor]
                            print(sabor_sel) 
                    break
                elif sabor_sel == "f":
                    for sabor in sabores:
                        if sabor == "FR":
                            sabor_sel = sabores[sabor]
                            print(sabor_sel) 
                    break
                elif sabor_sel == "l":
                    for sabor in sabores:
                        if sabor == "LI":
                            sabor_sel = sabores[sabor]
                            print(sabor_sel) 
                    break
                else:
                    print("No existe ese sabor")
        # Agregar el pedido a la lista de pedidos
        pedidos.append({sol_correo: sabor_sel})
        print("Pedido registrado exitosamente")
    except Exception as e:
        print(f"Lo sentimos, la entrada no fue valida: {e}")

# Definimos la función generar_reporte()
def generar_reporte():
    """Esta función genera un reporte de los pedidos"""
    try:
        if len(pedidos) == 0:
            print("No hay ningún pedido registrado")
            return
        else:
            print("""
                - C
                - V
                - F
                - L
                - Clientes sin pedidos""")
            seleccion = input("Seleccione una letra correspondiente al sabor").upper()
            if seleccion == "C":
                for sl in sabores:
                    seleccion = sabores[sl]
                    print(f"\t {seleccion}")
                    for pedido in pedidos:
                        for correo, sabor in pedido.items():
                            if sabor == seleccion:
                                print(f"\t - {correo}")
                if len(pedidos) == 0:
                    print("No hay pedidos registrados para este sabor")
            elif seleccion == "V":
                for sl in sabores:
                    seleccion = sabores[sl]
                    print(f"\t {seleccion}")
                    for pedido in pedidos:
                        for correo, sabor in pedido.items():
                            if sabor == seleccion:
                                print(f"\t - {correo}")
                if len(pedidos) == 0:
                    print("No hay pedidos registrados para este sabor")
            elif seleccion == "F":
                for sl in sabores:
                    seleccion = sabores[sl]
                    print(f"\t {seleccion}")
                    for pedido in pedidos:
                        for correo, sabor in pedido.items():
                            if sabor == seleccion:
                                print(f"\t - {correo}")
                if len(pedidos) == 0:
                    print("No hay pedidos registrados para este sabor")
            elif seleccion == "L":
                for sl in sabores:
                    seleccion = sabores[sl]
                    print(f"\t {seleccion}")
                    for pedido in pedidos:
                        for correo, sabor in pedido.items():
                            if sabor == seleccion:
                                print(f"\t - {correo}")
                if len(pedidos) == 0:
                    print("No hay pedidos registrados para este sabor")
                elif seleccion == "CLIENTES SIN PEDIDOS":
                    print("Clientes sin pedidos:")
                    clientes_con_pedidos = {list(pedido.keys())[0] for pedido in pedidos}
                    for correo in clientes:
                        if correo not in clientes_con_pedidos:
                            print(f"\t - {correo}")
                    if len(clientes_con_pedidos) == len(clientes):
                        print("Todos los clientes tienen pedidos registrados")
    except Exception as e:
        print(f"Lo sentimos, la entrada no fue valida: {e}")  