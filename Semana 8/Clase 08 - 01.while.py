"""inicio = 0
maximo = 5

while inicio < maximo:
    print("Saludo")
    inicio = inicio + 10"""

presupuesto = 1000
gasto = 0
while gasto <= presupuesto:
    compra = float(input("Digite el valor de compra: "))
    gasto += compra
gasto -= compra
print(gasto)

estado = "Conectado"
while estado == "Conectado":
    print("Hola Sebas")
    estado = input("Digite su estado: ")