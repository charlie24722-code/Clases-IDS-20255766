
import modulo_funciones1 as fn

# Definir función salir en main
def salir():
    """Esta función cierra el programa"""
    print("Gracias por usar el sistema. ¡Hasta luego!")
    exit()
def bienvenida():    
# Mostrar un menú que permita seleccionar opciones    
    print("""
    \t   Menu Principal
    \t 1. Registrar cliente
    \t 2. Registrar pedido
    \t 3. Ver reporte
    \t 4. Salir""")

    opcion = int(input("Seleccione una opción (1-4): "))
    if opcion == 1:
        fn.registrar_cliente()
    elif opcion == 2:
        fn.registrar_pedidos()
    elif opcion == 3:
        fn.generar_reporte()
    elif opcion == 4:
        salir()
    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")
bienvenida()