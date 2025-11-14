# Creare una función para registrar estudiantes
def registrar_estudiante(lista_estudiantes):
    """Esta función registra el nombre y carnet de los estudiantes"""
    nombre = input("Nombre: ")
    numeros = len(lista_estudiantes) + 1 
    if numeros < 10:
        carnet = "S00" + str(numeros)
    elif numeros < 100:
        carnet = "S0" + str(numeros)
    else: 
        carnet = "S" + str(numeros)
    estudiante = {"carnet": carnet,
                      "nombre": nombre}
    
    lista_estudiantes.append(estudiante)
    print(f"Estudiante registrado: {nombre} con carnet {carnet}")

# Creare esta función para mostrar los estudiantes
def mostrar_estudiantes(lista_estudiantes):
    """Esta función muestra los estudiantes que estan en la lista"""
    if len(lista_estudiantes) == 0:
        print("No hay ningun estudiante registrado")
        return
    else:
        print(lista_estudiantes)