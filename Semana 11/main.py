# Este es el inicio de mi sistema

# Importamos los moulos necesarios
import modulo_funciones as fn 

while True:
    print("""
          --Menu principal--
          1. Registrar estudiante
          2. Inscribir curso
          3. Generar reportes
          4. Salir
          """)
    opcion = input("Elija una opccion [1-4]")
    if opcion == "1":
        fn.registrar_estudiante()
    elif opcion == "2":
        print("Elegiste 2")
    elif opcion == "3":
        print("Elegiste 3")
    elif opcion == "4":
        print("Gracias, vuelva pronto")
        break
    else:
        print("La opcion no es valida.")
    