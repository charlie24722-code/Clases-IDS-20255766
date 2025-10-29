cantidad_personas = int(input())
edades = [int(input()) for _ in range (cantidad_personas)]
entrada = 0
for evaluación in edades:
    if evaluación > 15:
        entrada += 1
    
print(int(entrada))