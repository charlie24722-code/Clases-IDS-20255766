clientes = []
productos = []


cafeteria_inicio = True
while cafeteria_inicio:
    menu_principal = int(input("1. Mostrar productos, \n 2. Agregar productos, \n 3. Registrar nuevo cliente, \n 4.Mostrar clientes, \n 5. Registrar pedido, \n 6. Mostrar pedidos del día, \n 7. Mostrar categorías disponibles, \n 8. Salir"))
    if menu_principal == 1: 
        for ver in productos:
            print(ver)
    
