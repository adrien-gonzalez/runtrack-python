tab = []
for i in range(5):
    num = input("Entrer un chiffre ("+str(i)+") :")
    i = i + 1
    tab.append(num)
    if i == 5:
        print(sorted(tab))