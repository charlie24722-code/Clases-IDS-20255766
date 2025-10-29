cantidad_personas = int(input())
entrada = 0

for evaluación in range(cantidad_personas):
    edad = int(input())
    if edad >= 15:
        entrada += 1
    
print(int(entrada))