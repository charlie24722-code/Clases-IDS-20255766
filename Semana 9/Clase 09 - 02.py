usuarios = ["Ana", "Carlo", "Luis", "Maria", "Lorenzo"]
edades = [20, 19, 21, 22, 18]
frutas = ["mango", "fresa", "pera", "sandia", "piña"]

for usuario, edad, fruta in zip(usuarios, edades, frutas):
    print(f"El usuario {usuario}, con edad {edad}, le gusta {fruta}.")