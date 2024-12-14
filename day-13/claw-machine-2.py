import numpy as np
import re

f = open("./input.txt", "r")
# f = open("./example.txt", "r")
lines = f.readlines()


def find_nums(l):
    return [int(x) for x in re.findall('[0-9]+', l)]


machines = []
for i in range(0, len(lines), 4):
    a = find_nums(lines[i])
    b = find_nums(lines[i+1])
    prize = [x+10000000000000 for x in find_nums(lines[i+2])]
    machines.append((np.array([[a[0], b[0]], [a[1], b[1]]]),
                     np.array(prize)))

tok_sum = 0
for mach in machines:
    det = mach[0][0, 0] * mach[0][1, 1] - mach[0][0, 1] * mach[0][1, 0]
    res = np.array([[mach[0][1, 1], -mach[0][0, 1]],
                   [-mach[0][1, 0], mach[0][0, 0]]])@mach[1]
    if res[0] % det != 0 or res[1] % det != 0:
        print(res, mach, det)
        continue
    res //= det
    tok_sum += res[0] * 3 + res[1]
    print(res)

print("token used: "+str(tok_sum))
