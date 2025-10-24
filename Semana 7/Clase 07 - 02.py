"""numeros = ["uno", "dos", "tres", "cuatro"] #coleccion de elementos ordenados y mutables 
print(numeros[0])
print(numeros[1])
print(numeros[2])   
print(numeros[3])  
print(numeros.count("dos")) # .count() cuenta cuantas veces aparece un elemento en la lista"""

"""nombre = "Antonio"
print(nombre.lower().count("a")) # .lower() convierte todo a minusculas, .count("a") cuenta las letras "a" en el string"""

nombres = ["Ana", "Antonio", "Ana", "Jose"]
r_a = 0
r_a = r_a + nombres[0].lower().count("a")
r_a = r_a + nombres[1].lower().count("a")
r_a = r_a + nombres[2].lower().count("a")
r_a = r_a + nombres[3].lower().count("a")
print(r_a)
