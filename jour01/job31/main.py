def arrondi(tab):
    for i in range(len(tab)):
        j = 1
        while j <= 2:
            if ((tab[i]+j) % 5 == 0):
                tab[i] = tab[i]+j
            
            j = j + 1
        print(tab)
       
tab = [79, 80, 67, 54, 34, 23, 82, 83]
arrondi(tab)