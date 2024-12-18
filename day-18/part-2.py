from libaoc import *
import queue


Bytes = [findNums(l) for l in readfile()]

w, h = 7, 7

w, h = 71, 71

Map = [['.' for _ in range(w)] for _ in range(h)]


def BFS(Map, stx, sty, stn):
    q = queue.Queue()
    q.put((stx, sty, stn))
    while not q.empty():
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


i = 0
for x, y in Bytes:
    Map[y][x] = '#'
    MapPrint(Map)
    print(i)
    i += 1
    if i < 1024:
        continue
    nMap = MapCopy(Map)
    BFS(nMap, 0, 0, 0)
    if nMap[h-1][w-1] == '.':
        print("res: " + str(x) + "," + str(y))
        break
