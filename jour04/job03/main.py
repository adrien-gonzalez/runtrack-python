x = 2
def Puissance(n):
    if n == 1:
        return x
    else:
        return x*Puissance(n-1)


nombre = int(input('Renseignez un nombre entier : '))

print(Puissance(nombre))