# 1. Creare la función registrar libro
def registrar_libro(lista_libros):
    """Esta función registra los libros que se agregan"""
    titulo = input("Titulo: ")
    autor = input("Autor: ")
    numero = len(lista_libros) + 1 # sirve para generar el ccodigo e los libros automaticamente 
    if numero < 10:
        codigo = "L00" + str(numero)
    elif numero < 100:
        codigo = "L0" + str(numero)
    else: 
        codigo = "L" + str(numero) #entre más frande el numero, menos 0 tendra L a su derecha
        
    libro = {"codigo": codigo,
                  "titulo": titulo,
                  "autor": autor,
                  "disponible": True} #almaceno los datos en un diccionario para posteriormente agregarlos a la lista
    lista_libros.append(libro)


# creo una función para mostrar los libros
def mostrar_libros(lista_libros):
    """Muestra los libros registrados"""
    if len(lista_libros) == 0:
        print("No hay libros registrados")
        return # mostrar un mensaje en caso que no haya libros registrados y volver al inicio
    
    for libro in lista_libros:
        if libro["disponible"]:
            estado = "disponible" # verificcar que este disponible o no
        else:
            estado = "Prestado"
        print(f"El codigo del libro es: {libro["codigo"]}")
        print(f"El titulo es: {libro["titulo"]}")
        print(f"El autor es: {libro["autor"]}")
        print(f"El estado es: {estado}") # imprime los parametros registrados
   