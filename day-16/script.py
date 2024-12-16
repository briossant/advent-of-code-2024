import re
import functools as ft
import sys

sys.setrecursionlimit(15000)

f = open("./input.txt", "r")
# f = open("./example.txt", "r")
lines = f.readlines()

Map = [list(l.strip()) for l in lines]
w = len(Map[0])
h = len(Map)

st_x, st_y = 0, 0
ed_x, ed_y = 0, 0
for x in range(w):
    for y in range(h):
        if Map[y][x] == 'S':
            st_x = x
            st_y = y
        if Map[y][x] == 'E':
            ed_x = x
            ed_y = y


dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def run(x, y, last_d, cost):
    if Map[y][x] == '#':
        return
    if Map[y][x] == 'E':
        return
    if Map[y][x] == '.' or Map[y][x] == 'S' or Map[y][x] > cost:
        Map[y][x] = cost
    elif Map[y][x] != '.' and Map[y][x] != 'S' and Map[y][x] <= cost:
        return

    d = 0
    for (dx, dy) in dirs:
        if (d+2) % 4 == last_d:
            d += 1
            continue
        nx, ny = x+dx, y+dy
        nc = cost + (1 if d == last_d else 1001)
        run(nx, ny, d, nc)
        d += 1


run(st_x, st_y, 1, 0)


ends = [Map[ed_y+dy][ed_x+dx] for dx, dy in dirs]
res = 10000000000000
for e in ends:
    if e != '#' and e != '.' and e < res:
        res = e + 1

print('\n'.join([''.join([str(x) for x in l]) for l in Map]))

print("res: " + str(res))
