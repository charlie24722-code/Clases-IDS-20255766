palabra = input()
letra = input()

print(letra.casefold() == (palabra[-1::-1])[0].casefold())