import numpy as np

def findStart(a):
    pos =  np.where(a == '^')
    return (pos[0][0], pos[1][0])

def test(a):
    visited = set()
    currentPos = findStart(a)
    currentDir = (-1, 0)
    visited.add((currentPos, currentDir))

    shape = a.shape

    while True:
        newPos = (currentPos[0] + currentDir[0], currentPos[1] + currentDir[1])
        if newPos[0] < 0 or newPos[0] >= shape[0] or newPos[1] < 0 or newPos[1] >= shape[1]:
            return (False, visited)
        if a[newPos[0], newPos[1]] == '#':
            if currentDir == (-1, 0):
                currentDir = (0, 1)
            elif currentDir == (0, 1):
                currentDir = (1, 0)
            elif currentDir == (1, 0):
                currentDir = (0, -1)
            elif currentDir == (0, -1):
                currentDir = (-1, 0)
            continue

        if (newPos, currentDir) in visited:
            return (True, visited)
        
        currentPos = newPos
        visited.add((currentPos, currentDir))

f = open("input", "r")
lines = f.readlines()

a = np.array([list(line.strip()) for line in lines])
shape = a.shape

visited = set(map(lambda x: x[0],test(a)[1]))
print(len(visited))

part2 = 0
for i in range(shape[0]):
    for j in range(shape[1]):
        if a[i][j] == '.':
            copy = np.copy(a)
            copy[i][j] = '#'
            if test(copy)[0]:
                part2 += 1

print(part2)