import re
import matplotlib.pyplot as plt


f = open("../data.txt", "r")
words = re.findall("[\w']+", f.read().lower())

letters = {}
countLetter = 0   

for word in words:
    for lettre in word:
        if lettre in letters.keys():
            letters[lettre] += 1
        else:
            letters[lettre] = 1
            
        countLetter = countLetter + 1
 

for l in letters:
    letters[l] = (letters[l] * 100) / countLetter
    
    
x = letters.keys()
y = letters.values()
plt.bar(x,y)

plt.title('Pourcentage d’apparition de chaque lettre.', fontsize=10)

plt.savefig("plot_simple_histogramme_matplotlib_01.png")

plt.show()
