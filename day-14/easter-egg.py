import re
import functools as ft

f = open("./input.txt", "r")
# f = open("./example.txt", "r")
lines = f.readlines()

w = 101
h = 103


def find_nums(l):
    return [int(x) for x in re.findall('-?[0-9]+', l)]


robots = [find_nums(l) for l in lines]
sec = 0


def print_map():
    mom = [['.' for _ in range(w)] for _ in range(h)]
    for ro in robots:
        mom[ro[1]][ro[0]] = '#'
    print('\n'.join([''.join(l) for l in mom]))


while True:
    sec += 1
    q = [0, 0, 0, 0]
    for ro in robots:
        ro[0] = (ro[0] + ro[2]) % w
        ro[1] = (ro[1] + ro[3]) % h
        if ro[0] < w//2 and ro[1] < h//2:
            q[0] += 1
        elif ro[0] < w//2 and ro[1] > h//2:
            q[1] += 1
        elif ro[0] > w//2 and ro[1] < h//2:
            q[2] += 1
        elif ro[0] > w//2 and ro[1] > h//2:
            q[3] += 1
    for x in q:
        if x > len(robots)//2:
            print_map()
            print(sec)
