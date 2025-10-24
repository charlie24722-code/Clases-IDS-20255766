lista = [1,2, "tres", ["ene", "feb", "mar"]] # Las listas pueden teneer valores Heterogeneos
# lista.append(4) #.append agrega un elemento al final de la lista  

print(len(lista))
print(lista)
print(lista[2][2:].upper()) # Acceder a un elemento de la lista, en este caso el 3er elemento de la lista anidada "tres"
# como obtengo la a de marzo
print(lista[3][2][1]) # lista[3] accede a la lista anidada, [2] accede al elemento "mar" y [1] accede a la letra "a"
