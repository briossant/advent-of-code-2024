from libaoc import *
import pprint

Map = MapLoad()

w, h = len(Map[0]), len(Map)

NormalRace = MapCopy(Map)
BFS2(NormalRace, 'S', 'E')


def getDiff(x, y, offset):
    diffs = []
    for dx in range(-offset, offset):
        dy = abs(dx)-offset
        nx, ny = x+dx, y+dy

        if not MapIsOutOfBounds(Map, nx, ny) and type(NormalRace[ny][nx]) is int:
            d = NormalRace[ny][nx] - offset - NormalRace[y][x] - 1
            diffs.append(d + d % 2)

        dy = -dy
        nx, ny = x+dx, y+dy
        if dy != 0 and not MapIsOutOfBounds(Map, nx, ny) and type(NormalRace[ny][nx]) is int:
            d = NormalRace[ny][nx] - offset - NormalRace[y][x]
            diffs.append(d + d % 2)
    return diffs


MIN_SAVE = 50

shortcut = {}
ttshortcuts = 0
for x in range(1, w-1):
    print(x, w)
    for y in range(1, h-1):
        if Map[y][x] == '#':
            continue
        for offset in range(1, 21):
            diffs = getDiff(x, y, offset)
            for diff in diffs:
                if diff >= MIN_SAVE:
                    if diff in shortcut:
                        shortcut[diff] += 1
                    else:
                        shortcut[diff] = 1
                    ttshortcuts += 1

pprint.pprint(shortcut)
print("shortcuts:", ttshortcuts)
