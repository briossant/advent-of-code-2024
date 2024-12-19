import numpy as np
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
