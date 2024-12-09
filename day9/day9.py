import numpy as np


def prettyPrint(blocks):
    for block in blocks:
        if block[0]:
            print(block[1], end = "")
        else:
            print(".", end = "")
    print()

def prettyPrint2(blocks):
    for block in blocks:
        if block[0]:
            for i in range(block[2]):
                print(block[1], end = "")
        else:
            for i in range(block[2]):
                print(".", end = "")
    print()

f = open("input", "r")
data = f.read()

blocks = list()
part2Blocks = list()
isFile=True
id = 0
for v in data:
    #print(f"{isFile} {v}")
    if isFile:
        part2Blocks.append((isFile, id, int(v)))
    else:
        part2Blocks.append((isFile, None, int(v)))

    for c in range(int(v)):
        if isFile:
            blocks.append((isFile, id))
        else:
            blocks.append((isFile, None))
    
    if isFile:
        id += 1
    isFile = not isFile

    

part1Blocks = blocks.copy()
while True:
    try:
        firstEmptyIndex = part1Blocks.index((False, None))
        lastBlock = None
        while True:
            lastBlock = part1Blocks.pop()
            if lastBlock[0] == True:
                break
        part1Blocks[firstEmptyIndex] = lastBlock
    except:
        break

part1 = 0
for i, part1Blocks in enumerate(part1Blocks):
    part1 += i * part1Blocks[1]

print(f"Part1: {part1}")


blockToMoveIndex = len(part2Blocks) -1
while blockToMoveIndex > 0:
    blockToMove = None
    while True:
        blockToMove = part2Blocks[blockToMoveIndex]
        blockToMoveIndex -= 1
        if blockToMove[0] == True:
            break

    for i, block in enumerate(part2Blocks):
        if i >=  blockToMoveIndex + 1:
            break

        if block[0] == False and block[2] >= blockToMove[2]:
            if blockToMoveIndex+2 < len(part2Blocks) and part2Blocks[blockToMoveIndex+2][1] == False and part2Blocks[blockToMoveIndex][1] == False:
                #merge to next and prev
                part2Blocks[blockToMoveIndex+2] = (False, None, part2Blocks[blockToMoveIndex+2][2] + part2Blocks[blockToMoveIndex][2]+ blockToMove[2])
                part2Blocks.pop(blockToMoveIndex+1)
                part2Blocks.pop(blockToMoveIndex)
            elif blockToMoveIndex+2 < len(part2Blocks) and part2Blocks[blockToMoveIndex+2][1] == False:
                #merge to next
                part2Blocks[blockToMoveIndex+2] = (False, None, part2Blocks[blockToMoveIndex+2][2] + blockToMove[2])
                part2Blocks.pop(blockToMoveIndex+1)
            elif part2Blocks[blockToMoveIndex][1] == False:
                #merge to prev
                part2Blocks[blockToMoveIndex] = (False, None, part2Blocks[blockToMoveIndex][2] + blockToMove[2])
                part2Blocks.pop(blockToMoveIndex+1)
            else:
                #replace
                part2Blocks[blockToMoveIndex+1] = (False, None, blockToMove[2])

            part2Blocks[i] = blockToMove
            if blockToMove[2] < block[2]:
                part2Blocks.insert(i+1, (False, None, block[2] - blockToMove[2]))
                if i+1 <= blockToMoveIndex:
                    blockToMoveIndex += 1
            break

    #prettyPrint2(part2Blocks)

part2 = 0
pos = 0
for i, part2Block in enumerate(part2Blocks):
    if part2Block[0]:
        for i in range(pos, pos+part2Block[2]):
            part2 += i * part2Block[1]
    pos += part2Block[2]

print(f"Part2: {part2}")