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
    prize = find_nums(lines[i+2])
    machines.append((np.array([[a[0], b[0]], [a[1], b[1]]]),
                     np.array(prize)))

tok_sum = 0
tresh = 0.001
for mach in machines:
    try:
        res = np.linalg.inv(mach[0])@mach[1]
        if abs(round(res[0]) - res[0]) > tresh or abs(round(res[1] - res[1])) > tresh:
            continue
        res = [round(x) for x in res]
        if res[0] > 100 or res[1] > 100:
            continue
        tok_sum += res[0] * 3 + res[1]
        print(res)
    except Exception:
        continue

print("token used: "+str(tok_sum))
