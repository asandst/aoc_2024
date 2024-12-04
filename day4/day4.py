import numpy as np
import re

def findCountCol(a):
    return sum([len(re.findall("XMAS", ''.join(a[:,i]))) for i in range(a.shape[0])])

def findCountRow(a):
    return sum([len(re.findall("XMAS", ''.join(a[i,:]))) for i in range(a.shape[0])])

def findCountDiag(a):
    return sum([len(re.findall("XMAS", ''.join(a.diagonal(i)))) for i in range(a.shape[0])]) + sum([len(re.findall("XMAS", ''.join(a.diagonal(-i)))) for i in range(1, a.shape[0])])

def findMas(a):
    sum = 0
    for i in range(1, a.shape[0]-1):
        for j in range(1, a.shape[1]-1):
            if a[i][j] == 'A':
                if a[i-1][j-1] == 'M' and a[i+1][j-1] == 'M' and a[i-1][j+1] == 'S' and a[i+1][j+1] == 'S':
                    sum += 1

    return sum

f = open("input", "r")
lines = f.readlines()

a = np.array([list(line.strip()) for line in lines])

part1 = 0
part1 += findCountCol(a)
part1 += findCountRow(a)
part1 += findCountDiag(a)
part1 += findCountRow(np.fliplr(a))
part1 += findCountDiag(np.fliplr(a))
part1 += findCountCol(np.flipud(a))
part1 += findCountDiag(np.flipud(a))
part1 += findCountDiag(np.fliplr(np.flipud(a)))

print(part1)

part2 = 0
part2 += findMas(a)
part2 += findMas(np.fliplr(a))
part2 += findMas(a.transpose())
part2 += findMas(np.fliplr(a.transpose()))
print(part2)
