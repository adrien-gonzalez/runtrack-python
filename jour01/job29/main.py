def draw_triangle(hauteur):
    
    k = 1
    base = hauteur * 2
    j = hauteur
    p = 1
    
    
    while k <= hauteur:
        for i in range(j):
            print(' ', end='')
        
        if k == hauteur:
            print('/', end='')
            while p < base - 1:
                print('_', end='')
                p = p + 1
        else:    
            print('/', end='')

        if k > 1 and k != hauteur:
            i = 1.5
            while i <= k:
                print(' ', end='')
                i = i + 0.5
            
        print('\\')
        k = k + 1
        j = j - 1
      

hauteur = int(input("Entrer une hauteur : "))
draw_triangle(hauteur)