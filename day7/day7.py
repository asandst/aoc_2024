import re
import itertools

def test(ops, parsedLine):
    sum = -1
    for i, v in enumerate(parsedLine[1]):
        if i == 0:
            sum = v
        else:
            if ops[i-1] == '+':
                sum += v
            elif ops[i-1] == '*':
                sum *= v
            elif ops[i-1] == '|':
                sum = int(str(sum) + str(v))

    return sum == parsedLine[0]

def concat(ops, parsedLine):
    for i, op in enumerate(ops):
        if op == '|':
            newOps = ops[:i] + ops[i+1:]

            currValue = parsedLine[1][i]
            nextValue = parsedLine[1][i+1]
            merged = int(str(currValue) + str(nextValue))
            newParsedLine = parsedLine[1][:i] + list([merged]) + parsedLine[1][i+2:]
            print(f"{ops} {newOps} {parsedLine} {newParsedLine}")
            return concat(newOps, (parsedLine[0], newParsedLine))
        
    return (ops, parsedLine)

f = open("input", "r")
lines = f.readlines()

parsedLines = list()

for line in lines:
    lineParts = line.split(':')
    sum = int(lineParts[0])
    parts = list(map(int, lineParts[1].strip().split(' ')))
    parsedLines.append((sum, parts))
#print(parsedLines)

part1 = 0
for parsedLine in parsedLines:
    numOps = len(parsedLine[1])-1
    iter = itertools.product("+*", repeat=numOps)
    for i in iter:
        if test(i, parsedLine):
            part1 += parsedLine[0]
            #print(f"{i} {parsedLine}")
            break
print(part1)

part2 = 0
for parsedLine in parsedLines:
    numOps = len(parsedLine[1])-1
    iter = itertools.product("+*|", repeat=numOps)
    for i in iter:
        #(i2, parsedLine2) = concat(i, parsedLine)
        #print(f"Concated {i} {i2} {parsedLine} {parsedLine2}")
        if test(i, parsedLine):
            part2 += parsedLine[0]
            #print(f"True {i} {i2} {parsedLine} {parsedLine2}")
            break
print(part2)