def blink(stone, itersLeft, map):
    if itersLeft == 0:
        return 1
    
    if (stone, itersLeft) in map:
        return map[(stone, itersLeft)]
    
    res = 0
    if stone == "0":
        res = blink("1", itersLeft-1, map)
    elif len(stone) % 2 == 0:
        left = str(int(stone[:int(len(stone)/2)]))
        right = str(int(stone[int(len(stone)/2):]))
        res = blink(left, itersLeft-1, map) + blink(right, itersLeft-1, map)
    else:
        res = blink(str(int(stone) * 2024), itersLeft-1, map)

    map[(stone, itersLeft)] = res
    return res    

f = open("input", "r")
line = f.read()

stones = line.split()
part1 = 0
part2 = 0
map = dict()
for stone in stones:
    part1 += blink(stone, 25, map)
    part2 += blink(stone, 75, map)
    
print(part1)
print(part2)