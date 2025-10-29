# Iterable: Objeto capaz de devolver sus compnetnes uno a la vez
# Iterador: Es un objeto que representa un flujo de datos
nombres = ["Ana", "Sebas", "Mario", "Carla"]
# Encontremos a Sebas
nombre_buscar = input("Nombre a buscar: ")
for n in nombres:
    if n == nombre_buscar:
        print("Ya lo encontre")
    else:
        print("Aqui no esta")