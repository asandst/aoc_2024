import numpy as np
import itertools

f = open("input", "r")
lines = f.readlines()

a = np.array([list(line.strip()) for line in lines])

possibleFreqs = itertools.chain(range(ord('a'), ord('z')+1), range(ord('A'), ord('Z')+1), range(ord('0'), ord('9')+1))
antiNodes = set()

for freq in possibleFreqs:
    antennasRaw = np.where(a == chr(freq))

    antennas = list(zip(antennasRaw[0], antennasRaw[1]))
    if len(antennas) > 0:
        permutations = itertools.permutations(antennas, 2)
        for p in permutations:
            if p[0][0] < p[1][0]:
                diff = (p[1][0] - p[0][0], p[1][1] - p[0][1])
                first = (p[0][0] - diff[0], p[0][1] - diff[1])
                second = (p[1][0] + diff[0], p[1][1] + diff[1])
                if first[0] >= 0 and first[0] < a.shape[0] and first[1] >= 0 and first[1] < a.shape[1]: 
                    antiNodes.add(first)
                if second[0] >= 0 and second[0] < a.shape[0] and second[1] >= 0 and second[1] < a.shape[1]: 
                    antiNodes.add(second)

print(f"Part1: {len(antiNodes)}")

possibleFreqs = itertools.chain(range(ord('a'), ord('z')+1), range(ord('A'), ord('Z')+1), range(ord('0'), ord('9')+1))
antiNodes = set()

for freq in possibleFreqs:
    antennasRaw = np.where(a == chr(freq))

    antennas = list(zip(antennasRaw[0], antennasRaw[1]))
    if len(antennas) > 0:
        permutations = itertools.permutations(antennas, 2)
        for p in permutations:
            if p[0][0] < p[1][0]:
                diff = (p[1][0] - p[0][0], p[1][1] - p[0][1])

                for multiplicator in [-1, 1]:
                    for i in range(0, 1000):
                        antiNode = (p[0][0] + multiplicator*i*diff[0], p[0][1] + multiplicator*i*diff[1])
                        if antiNode[0] >= 0 and antiNode[0] < a.shape[0] and antiNode[1] >= 0 and antiNode[1] < a.shape[1]: 
                            antiNodes.add(antiNode)
                        else:
                            break

print(f"Part2: {len(antiNodes)}")