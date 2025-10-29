N = int(input())
for amore in range(N):
    nombre = input()
    letras = len(nombre)
    if letras <= 6:
        print("No vale la pena")
    elif letras == 7:
        print("Dios no creo aguantar esta vez")
    else:
        print("Si aguanto otro desarrollo de personaje")
        