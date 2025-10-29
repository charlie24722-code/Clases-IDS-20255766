# Leer cantidad de combos
n = int(input())

# Leer daño de cada ataque
linea = input().split()
pa = int(linea[0])
pb = int(linea[1])
pc = int(linea[2])

# Procesar cada combo
for golpes in range(n):
    combo = input().strip()
    
    # Calcular daño total del combo
    danio_total = 0
    for ataque in combo:
        if ataque == 'A':
            danio_total += pa
        elif ataque == 'B':
            danio_total += pb
        elif ataque == 'C':
            danio_total += pc
    
    print(danio_total)