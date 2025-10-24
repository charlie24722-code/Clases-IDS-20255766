nombres = ["Ana", "Antonio", "Paulina", "Jose"]
print(nombres)
nombres[2] = "Pablo"
print(nombres)
nombres.append(input("Ingrese el nuevo nombre: "))
print(nombres)
(nombres.insert(int(input("Indique el indice: ")), input("Nombre: ")))
print(nombres)
nombres.remove("Sebas")
print(nombres)
nombre_borrado = nombres.pop(int(input("indice a borrar: "))-1)
print(nombres)
print(nombre_borrado)