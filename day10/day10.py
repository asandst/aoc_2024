import numpy as np

def visitPart1(topoMap, visited, node, tops):
    visited.add(str(node))
    if topoMap[node[0]][node[1]] == 9:
        tops.add(str(node))
        return

    neighbours = node + neighboursOffsets
    for neighbour in neighbours:
        if neighbour[0] >= 0 and neighbour[0] < topoMap.shape[0] and neighbour[1] >= 0 and neighbour[1] < topoMap.shape[1]:
            if not str(neighbour) in visited and topoMap[neighbour[0]][neighbour[1]] == topoMap[node[0]][node[1]]+1:
                visitPart1(topoMap, visited, neighbour, tops)

def visitPart2(topoMap, visited, node, trails, trail):
    visited.add(str(trail))
    if topoMap[node[0]][node[1]] == 9:
        trails.add(str(trail))
        return

    neighbours = node + neighboursOffsets
    for neighbour in neighbours:
        if neighbour[0] >= 0 and neighbour[0] < topoMap.shape[0] and neighbour[1] >= 0 and neighbour[1] < topoMap.shape[1]:
            newTrail = trail.copy()
            newTrail.append(neighbour)
            if not str(newTrail) in visited and topoMap[neighbour[0]][neighbour[1]] == topoMap[node[0]][node[1]]+1:
                visitPart2(topoMap, visited, neighbour, trails, newTrail)

f = open("input", "r")
lines = f.readlines()
topoMap = np.array([list(map(int,list(line.strip()))) for line in lines])
trailHeadsRaw = np.where(topoMap == 0)
trailHeads = np.array(list(zip(trailHeadsRaw[0], trailHeadsRaw[1])))
neighboursOffsets = [(0,1), (0, -1), (1, 0), (-1, 0)]

part1 = 0
part2 = 0
for trailHead in trailHeads:
    visited = set()
    tops = set()
    trails = set()
    visitPart1(topoMap, visited, trailHead, tops)
    part1 += len(tops)
    visitPart2(topoMap, visited, trailHead, trails, list(trailHead))
    part2 += len(trails)

print(f"Part1: {part1}")
print(f"Part2: {part2}")