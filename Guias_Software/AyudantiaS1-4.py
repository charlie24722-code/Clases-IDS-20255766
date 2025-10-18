contraseña = int(input())

A = input() 
B = input()

print(A[:len(A)//contraseña] + B[-len(B)//contraseña:])