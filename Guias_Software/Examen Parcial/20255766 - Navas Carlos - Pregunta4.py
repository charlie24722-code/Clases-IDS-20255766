palindromo = input()

print(palindromo.casefold() == palindromo[-1::-1].casefold())