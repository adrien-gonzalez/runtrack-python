import re

f = open("../domains.xml", "r")
domains = re.findall('[.]{1}[a-z]{2,4}<', f.read())
nameDomains = []

i = 0
while i < len(domains):
    if domains[i] not in nameDomains:
        nameDomains.append(domains[i])
    i = i + 1


print(nameDomains)


