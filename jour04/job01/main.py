def Factorial(n):
    if n == 0:
        return 1
    else:
        return n*Factorial(n-1)


nombre = int(input('Renseignez un nombre entier : '))

print(Factorial(nombre))