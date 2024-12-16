import re
import queue
import functools as ft
import sys

sys.setrecursionlimit(15000)

f = open("./input.txt", "r")
# f = open("./example02.txt", "r")
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
            Map[y][x] = 0
        if Map[y][x] == 'E':
            ed_x = x
            ed_y = y


dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def run():
    q = queue.Queue()
    q.put((st_x, st_y, 1, 0))
    while not q.empty():
        x, y, last_d, cost = q.get()

        d = 0
        for (dx, dy) in dirs:
            d += 1
            if (d+1) % 4 == last_d:
                continue
            nx, ny = x+dx, y+dy
            nc = cost + (1 if d-1 == last_d else 1001)
            if Map[ny][nx] == '#' or Map[ny][nx] == 'E':
                continue
            if Map[ny][nx] == '.' or Map[ny][nx] > nc:
                Map[ny][nx] = nc
            elif Map[ny][nx] != '.' and Map[ny][nx] <= nc:
                continue
            q.put((nx, ny, d-1, nc))


def backrun(nMap, x, y, cost, last_c):
    nMap[y][x] = 'O'
    for (dx, dy) in dirs:
        ny, nx = y+dy, x+dx
        if Map[ny][nx] != '#' and Map[ny][nx] != '.':
            if Map[ny][nx] < cost or ((Map[ny][nx] == last_c-1002 or Map[ny][nx] == last_c-2) and last_c != -1):
                backrun(nMap, nx, ny, Map[ny][nx], cost)


run()


ends = [Map[ed_y+dy][ed_x+dx] for dx, dy in dirs]
res = 10000000000000
for e in ends:
    if e != '#' and e != '.' and e < res:
        res = e + 1
Map[ed_y][ed_x] = res

print('\n'.join(
    [''.join([format(x, '05d') if x != 'O' and x != '#' else x+'====' for x in l]) for l in Map]))

print("res: " + str(res))

nMap = [[x for x in l] for l in Map]

backrun(nMap, ed_x, ed_y, Map[ed_y][ed_x], -1)

print('\n'.join(
    [''.join(['.' if x != 'O' and x != '#' else x for x in l]) for l in nMap]))
res = sum([l.count('O') for l in nMap])

print("res: " + str(res))
