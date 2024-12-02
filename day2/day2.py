import numpy as np

def test(n):
    n_diff = np.diff(n)
    pos = (n_diff >= 0).all()
    neg = (n_diff <= 0).all()
    gt0 = (abs(n_diff) >= 1).all() 
    lte3 = (abs(n_diff) <= 3).all() 
    return (pos | neg) & gt0 & lte3

def part2_test(n):
    return np.array([test(np.delete(n, i)) for i in range(n.size)]).any()

f = open("input", "r")
lines = f.readlines()
part1 = 0
part2 = 0
for line in lines:
    numbers = [int(s) for s in line.split()]
    n = np.array(numbers)
    part1 += test(n)
    part2 += part2_test(n)

print(part1)
print(part2)