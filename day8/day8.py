import numpy as np
import itertools

f = open("input", "r")
lines = f.readlines()
antennaMap = np.array([list(line.strip()) for line in lines])
part1 = set()
part2 = set()
possibleFreqs = itertools.chain(range(ord('a'), ord('z')+1), range(ord('A'), ord('Z')+1), range(ord('0'), ord('9')+1))

for freq in possibleFreqs:
    antennasRaw = np.where(antennaMap == chr(freq))
    antennas = list(zip(antennasRaw[0], antennasRaw[1]))
    if len(antennas) > 0:
        permutations = itertools.permutations(antennas, 2)
        for p in permutations:
            diff = (p[1][0] - p[0][0], p[1][1] - p[0][1])
            for i in range(0, 1000):
                antiNode = (p[0][0] - i*diff[0], p[0][1] - i*diff[1])
                if antiNode[0] >= 0 and antiNode[0] < antennaMap.shape[0] and antiNode[1] >= 0 and antiNode[1] < antennaMap.shape[1]: 
                    if i == 1:
                        part1.add(antiNode)
                    part2.add(antiNode)
                else:
                    break
print(f"Part1: {len(part1)}")
print(f"Part2: {len(part2)}")