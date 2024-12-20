from libaoc import *
import pprint

Map = MapLoad()

w, h = len(Map[0]), len(Map)

NormalRace = MapCopy(Map)
BFS2(NormalRace, 'S', 'E')


def getDiff(CheatPath, st_time):
    diffs = []
    ends = []
    for x in range(w):
        for y in range(h):
            if type(CheatPath[y][x]) is not int:
                continue

            for dx, dy in cross_dirs:
                nx, ny = x+dx, y+dy
                if MapIsOutOfBounds(Map, nx, ny) or type(NormalRace[ny][nx]) is not int:
                    continue

                d = NormalRace[ny][nx] - st_time - CheatPath[y][x] - 1
                if (nx, ny) in ends:
                    i = ends.index((nx, ny))
                    if diffs[i] < d:
                        diffs[i] = d
                else:
                    diffs.append(d)
                    ends.append((nx, ny))
    return diffs


MIN_SAVE = 50

shortcut = {}
ttshortcuts = 0
for x in range(1, w-1):
    print(x, w)
    for y in range(1, h-1):
        if Map[y][x] == '#':
            continue
        CheatPath = MapCopy(Map)
        BFS(CheatPath, x, y, gdchars=['#', '.'], max_n=20)
        diffs = getDiff(CheatPath, NormalRace[y][x])
        for diff in diffs:
            if diff >= MIN_SAVE:
                if diff in shortcut:
                    shortcut[diff] += 1
                else:
                    shortcut[diff] = 1
                ttshortcuts += 1

pprint.pprint(shortcut)
print("shortcuts:", ttshortcuts)
