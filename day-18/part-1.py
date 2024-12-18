from libaoc import *
import queue


Bytes = [findNums(l) for l in readfile()]

Bytes_to_write = 12
w, h = 7, 7

Bytes_to_write = 1024
w, h = 71, 71

Map = [['.' for _ in range(w)] for _ in range(h)]


i = 0
for x, y in Bytes:
    if i == Bytes_to_write:
        break
    i += 1
    Map[y][x] = '#'


def BFS(Map, stx, sty, stn):
    q = queue.Queue()
    q.put((stx, sty, stn))
    i = 0
    while not q.empty():
        i += 1
        if i % 1000 == 0:
            MapPrint(Map)
            print(i)
        (x, y, n) = q.get()
        for dx, dy in cross_dirs:
            nx, ny = x+dx, y+dy
            nn = n+1
            if MapIsOutOfBounds(Map, nx, ny) or Map[ny][nx] != '.':
                continue
            Map[ny][nx] = nn
            if x == w-1 and y == h-1:
                return
            q.put((nx, ny, nn))


MapPrint(Map)
BFS(Map, 0, 0, 0)

MapPrint(Map)

print("res:", Map[h-1][w-1])
