import re

f = open("input", "r")
data = f.read()
matches = re.findall("mul\((\d+),(\d+)\)", data)

part1 = 0
for x,y in matches:
    part1 += int(x)*int(y)
print(f"part1: {part1}")

matches = re.findall("mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))", data)
enabled = True
part2 = 0
for x,y,do,dont in matches:
    if dont:
        enabled = False
    elif do:
        enabled = True
    elif x and enabled:
        part2 += int(x)*int(y)
print(f"part2: {part2}")