from libaoc import *
import queue

Map = MapLoad()
w = len(Map[0])
h = len(Map)

st_x, st_y = MapFind(Map, 'S')
ed_x, ed_y = MapFind(Map, 'E')
Map[st_y][st_x] = 0


def run():
    q = queue.Queue()
    q.put((st_x, st_y, 2, 0))
    while not q.empty():
        x, y, last_d, cost = q.get()

        d = 0
        for (dx, dy) in cross_dirs:
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
    for (dx, dy) in cross_dirs:
        ny, nx = y+dy, x+dx
        if Map[ny][nx] != '#' and Map[ny][nx] != '.':
            if Map[ny][nx] < cost or ((Map[ny][nx] == last_c-1002 or Map[ny][nx] == last_c-2) and last_c != -1):
                backrun(nMap, nx, ny, Map[ny][nx], cost)


run()


ends = [Map[ed_y+dy][ed_x+dx] for dx, dy in cross_dirs]
res = 10000000000000
for e in ends:
    if e != '#' and e != '.' and e < res:
        res = e + 1
Map[ed_y][ed_x] = res

MapPrint(Map, lambda x:
         format(x, '05d') if type(x) is int else x+'====')

print("res: " + str(res))

nMap = MapCopy(Map)
backrun(nMap, ed_x, ed_y, Map[ed_y][ed_x], -1)

MapPrint(nMap, lambda x: '.' if x != 'O' and x != '#' else x)

res = MapCount(nMap, 'O')

print("res: " + str(res))
