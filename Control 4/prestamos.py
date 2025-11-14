# Creare una función para registrar prestamos

def registrar_prestamo(lista_libros,lista_estudiantes,lista_prestamos):
    """Esta función registra los prestamos que realizan los estudiantes"""
    carnet = input("Ingrese su numero de carnet: ")
    encontrado = False
    for estudiante in lista_estudiantes:
        if estudiante["carnet"] == carnet:
            encontrado = True   
            print("Este carnet esta registrado") # para buscar y encontrar el carnet que ha sido ingresado
    if encontrado == False:
            print("Este carnet no esta registrado")
            return # devuelve al inicio si el carnet no ha sido registrado
      
    codigo = input("Ingrese el código del libro a prestrar: ")        
    libro_prestar = {} # diccionario vacio para registrar información
    for libro in lista_libros:
        if libro["codigo"] == codigo:
            libro_prestar = libro # inserta la información extraida de la lista_libros despues de verificarse que los codigos sean iguales
    if len(libro_prestar) == 0:
        print("Este código no pertenece a ningun libro")
        return # verifica si el codigo es válido
    else:
        print("El libro fue encontrado con éxito")    
    if libro_prestar["disponible"] == False:
        print("Este libro ya ha sido prestado")
        return # verifica si el libro ha sido prestado 
    
    fecha = input("Ingrese la fecha del prestamo (ej:dd/mm/aa): ")
    prestamo = {"carnet_estu": carnet,
                "codigo_libro": codigo,
                "fecha": fecha} # guarda la información que ha sido registrada anteriormente
    lista_prestamos.append(prestamo) # añade el diccionario a la lista
    libro_prestar["disponible"] = False
    print("Prestamo registrado exitosamente") # cambia el estado de disponibildad para que el libro prestado ya no este disponible

# Creare una función para mostrar prestamos
def mostrar_prestamos(lista_prestamos):
    """Esta función muestra los prestamos que estan en curso"""
    if len(lista_prestamos) == 0: # verifica si hay prestamos
        print("No hay prestamos en curso") 
        return
    else:
        print(lista_prestamos)