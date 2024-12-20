import numpy as np
import queue
import re
import sys

sys.setrecursionlimit(42000)

cross_dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
diag_dirs = [(-1, -1), (1, 1), (1, -1), (-1, 1)]
full_dirs = [(-1, 0), (0, 1), (1, 0), (0, -1),
             (-1, -1), (1, 1), (1, -1), (-1, 1)]


def readfile(no_strip=False):
    if len(sys.argv) < 2:
        print("Usage: python " + sys.argv[0] + " [input filename]")
        exit(1)
    f = open(sys.argv[1], "r")
    if no_strip:
        return f.readlines()
    return [l.strip() for l in f.readlines()]


def MapLoad():
    return [list(l.strip()) for l in readfile()]


def MapPrint(Map, fm=lambda x: str(x)):
    print('\n'.join([''.join([fm(x) for x in l]) for l in Map]))


def MapCopy(Map):
    return [[x for x in l] for l in Map]


def MapCount(Map, e):
    return sum([l.count(e) for l in Map])


def MapFind(Map, e):
    for y in range(len(Map)):
        for x in range(len(Map[y])):
            if Map[y][x] == e:
                return x, y
    return -1, -1


def findNums(l):
    return [int(x) for x in re.findall('[0-9]+', l)]


def MapIsOutOfBounds(Map, x, y):
    return x < 0 or y < 0 or x >= len(Map[0]) or y >= len(Map)


def BFS2(Map, stchar, edchar, gdchars=['.'], stn=0):
    stx, sty = MapFind(Map, stchar)
    edx, edy = MapFind(Map, edchar)
    gdchars.append(edchar)
    BFS(Map, stx, sty, edx, edy, gdchars, stn)


def BFS(Map, stx, sty, edx=-1, edy=-1, gdchars=['.'], stn=0, max_n=-1):
    q = queue.Queue()
    q.put((stx, sty, stn))
    w, h = len(Map[0]), len(Map)
    Map[sty][stx] = stn
    while not q.empty():
        (x, y, n) = q.get()
        for dx, dy in cross_dirs:
            nx, ny = x+dx, y+dy
            nn = n+1
            if max_n > 0 and nn >= max_n:
                return
            if MapIsOutOfBounds(Map, nx, ny) or Map[ny][nx] not in gdchars:
                continue
            Map[ny][nx] = nn
            if x == edx and y == edy:
                return
            q.put((nx, ny, nn))
