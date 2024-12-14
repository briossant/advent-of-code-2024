import re
import functools as ft

f = open("./input.txt", "r")
# f = open("./example.txt", "r")
lines = f.readlines()

w = 101
h = 103
sec = 100


def find_nums(l):
    return [int(x) for x in re.findall('-?[0-9]+', l)]


robots = [find_nums(l) for l in lines]

for i in range(sec):
    for ro in robots:
        ro[0] = (ro[0] + ro[2]) % w
        ro[1] = (ro[1] + ro[3]) % h

q1, q2, q3, q4 = 0, 0, 0, 0
for ro in robots:
    if ro[0] < w//2 and ro[1] < h//2:
        q1 += 1
    elif ro[0] < w//2 and ro[1] > h//2:
        q2 += 1
    elif ro[0] > w//2 and ro[1] < h//2:
        q3 += 1
    elif ro[0] > w//2 and ro[1] > h//2:
        q4 += 1

print("nbr of robots: "+str(q1*q2*q3*q4))
