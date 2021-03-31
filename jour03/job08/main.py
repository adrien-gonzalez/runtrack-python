import re
import matplotlib.pyplot as plt


f = open("../data.txt", "r")
words = re.findall("[\w']+", f.read().lower())

wordsLength = {}
countword = 0

for word in words:
    if len(word) in wordsLength.keys():
        wordsLength[len(word)] += 1
    else:
        wordsLength[len(word)] = 1
    
    countword = countword + 1
 

for l in wordsLength:
    wordsLength[l] = (wordsLength[l] * 100) / countword
    

    
x = wordsLength.keys()
y = wordsLength.values()

plt.xlabel("Nombre de lettres")
plt.ylabel("Nombre de mots")
plt.bar(x,y)


plt.title('Pourcentage d’apparition de chaque lettre.', fontsize=10)

plt.savefig("plot_simple_histogramme_matplotlib_01.png")

plt.show()