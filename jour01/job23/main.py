def draw_rectangle(a, b):
    j = 1
    k = 1
    
    while k <= b:
        if k == 1 or k == b:
            print('|', end='')
            i = 1
            while i <= a:
                if i == a:
                    print('-|')
                else:
                    print('-', end='')
                
                i = i + 1
        else:
            while j <= a:
                if j == a:
                    print(' |')
                elif j == 1:
                    print('| ', end='')
                else:
                    print(' ', end='')
                j = j + 1
        
        k = k + 1
            
tab = []
for i in range(2):
    if i == 0:
        num = int(input("Entrer une largeur : "))
    else:
        num = int(input("Entrer une longueur : "))
    
    tab.append(num)
    
    
draw_rectangle(tab[0], tab[1])
