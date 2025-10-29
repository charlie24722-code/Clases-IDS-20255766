Valores = [[1,3,6],
            [2,7,4], 
            [6,5,9], 
            [1,10,20]]

minimo = int(input("digite el minimo: "))
mayores = []
for v in Valores:
    for reales in v:
        if reales > minimo:
            mayores.append(reales)
            
print(mayores)