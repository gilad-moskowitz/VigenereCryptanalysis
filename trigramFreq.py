import math

with open('english_trigrams.txt') as trigrams:
    triLine = trigrams.readlines()
final = [a.replace('\n', '') for a in triLine]

total = 0
for a in final:
    total += int(a[4:])
trigramLogFreq = {}
for tri in final:
    trigramLogFreq[tri[0:3].lower()] = math.log(int(tri[4:])/total)