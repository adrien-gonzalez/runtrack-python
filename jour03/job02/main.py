import re
f = open("../data.txt", "r")

words = re.findall("[\w']+", f.read())
print(len(words))