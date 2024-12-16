import numpy as np
import re
import sys

sys.setrecursionlimit(42000)

cross_dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
diag_dirs = [(-1, -1), (1, 1), (1, -1), (-1, 1)]
full_dirs = [(-1, 0), (0, 1), (1, 0), (0, -1),
             (-1, -1), (1, 1), (1, -1), (-1, 1)]


def readfile():
    if len(sys.argv) < 2:
        print("Usage: python " + sys.argv[0] + " [input filename]")
        exit(1)
    f = open(sys.argv[1], "r")
    return f.readlines()


def loadMap():
    return [list(l.strip()) for l in readfile()]


def printMap(Map, fm=lambda x: str(x)):
    print('\n'.join([''.join([fm(x) for x in l]) for l in Map]))


def copyMap(Map):
    return [[x for x in l] for l in Map]


def countInMap(Map, e):
    return sum([l.count(e) for l in Map])


def findInMap(Map, e):
    for y in range(len(Map)):
        for x in range(len(Map[y])):
            if Map[y][x] == e:
                return x, y
    return -1, -1
