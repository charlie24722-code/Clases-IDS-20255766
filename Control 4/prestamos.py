# Creare una función para registrar prestamos

def registrar_prestamo(lista_libros,lista_estudiantes,lista_prestamos):
    """Esta función registra los prestamos que realizan los estudiantes"""
    carnet = input("Ingrese su numero de carnet: ")
    encontrado = False
    for estudiante in lista_estudiantes:
        if estudiante["carnet"] == carnet:
            encontrado = True   
            print("Este carnet esta registrado")      
    if encontrado == False:
            print("Este carnet no esta registrado")
            return
      
    codigo = input("Ingrese el código del libro a prestrar: ")        
    libro_prestar = {}
    for libro in lista_libros:
        if libro["codigo"] == codigo:
            libro_prestar = libro
    if len(libro_prestar) == 0:
        print("Este código no pertenece a ningun libro")
        return
    else:
        print("El libro fue encontrado con éxito")    
    if libro_prestar["disponible"] == False:
        print("Este libro ya ha sido prestado")
        return
    
    fecha = input("Ingrese la fecha del prestamo (ej:dd/mm/aa): ")
    prestamo = {"carnet_estu": carnet,
                "codigo_libro": codigo,
                "fecha": fecha}
    lista_prestamos.append(prestamo)
    libro_prestar["disponible"] = False
    print("Prestamo registrado exitosamente")

# Creare una función para mostrar prestamos
def mostrar_prestamos(lista_prestamos):
    """Esta función muestra los prestamos que estan en curso"""
    if len(lista_prestamos) == 0:
        print("No hay prestamos en curso")
        return
    else:
        print(lista_prestamos)