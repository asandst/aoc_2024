import re

def isValid(m, row):
    for i, value in enumerate(row):
        if value in m:
            before = m[value]
            for b in before:
                if b in row and row.index(b) < i:
                    return (row.index(b), i)
    return True

f = open("input", "r")
lines = f.readlines()

firstParsePart = True

m = dict()
rows = list()
for line in lines:
    if line.strip() == '':
        firstParsePart=False
        continue
    if firstParsePart:
        for a,b in re.findall("(\d+)\|(\d+)", line):
            if a in m:
                m[a].append(b)
            else:
                m[a] = list()
                m[a].append(b)
    else:
        rows.append(line.strip().split(','))

part1 = 0
for row in rows:
    valid = isValid(m, row)
    if valid == True:
        part1 += int(row[int(len(row)/2)])

print(part1)

part2 = 0
for row in rows:
    valid = isValid(m, row)
    if valid == True:
        continue

    while valid != True:
        row.insert(valid[1], row.pop(valid[0]))
        valid = isValid(m, row)
    part2 += int(row[int(len(row)/2)])

print(part2)
        


        
