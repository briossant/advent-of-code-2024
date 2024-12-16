import re
import functools as ft
import sys

sys.setrecursionlimit(15000)

# f = open("./input.txt", "r")
f = open("./example02.txt", "r")
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
    elif Map[y][x] != '.' and Map[y][x] != 'S' and Map[y][x] < cost:
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


def backrun(x, y, cost, last_c):
    Map[y][x] = 'O'
    for (dx, dy) in dirs:
        ny, nx = y+dy, x+dx
        if Map[ny][nx] != '#' and Map[ny][nx] != '.' and Map[ny][nx] != 'O':
            if Map[ny][nx] < cost or ((Map[ny][nx] == last_c-1002 or Map[ny][nx] == last_c-2) and last_c != -1):
                backrun(nx, ny, Map[ny][nx], cost)


run(st_x, st_y, 1, 0)


ends = [Map[ed_y+dy][ed_x+dx] for dx, dy in dirs]
res = 10000000000000
for e in ends:
    if e != '#' and e != '.' and e < res:
        res = e + 1
Map[ed_y][ed_x] = res

print('\n'.join(
    [''.join([format(x, '05d') if x != 'O' and x != '#' else x+'====' for x in l]) for l in Map]))

print("res: " + str(res))

backrun(ed_x, ed_y, Map[ed_y][ed_x], -1)

print('\n'.join(
    [''.join(['.' if x != 'O' and x != '#' else x for x in l]) for l in Map]))
res = sum([l.count('O') for l in Map])

print("res: " + str(res))
