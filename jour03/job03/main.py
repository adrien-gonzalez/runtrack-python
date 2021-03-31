import re

taille = int(input('Rentrez un nombre entier : '))
count = 0

f = open("../data.txt", "r")
words = re.findall("[\w']+", f.read())

i = 0
while i < len(words):
    if len(words[i]) == taille:
        count += 1
    i += 1
    
print(count)
