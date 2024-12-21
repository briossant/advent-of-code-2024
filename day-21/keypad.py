from libaoc import *
import pprint as pp

num_keypad_paths = {}
num_keypad = ["987", "654", "321", "A0"]

dir_keypad_paths = {}
dir_keypad = ["A^", ">v<"]


def MakePath(keypad, stx, sty, edx, edy):
    if stx == edx and sty == edy:
        return ["A"]

    path = []
    if stx < edx and stx+1 < len(keypad[sty]):
        t = MakePath(keypad, stx+1, sty, edx, edy)
        t = ["<" + s for s in t]
        path.extend(t)
    elif stx > edx and stx-1 >= 0:
        t = MakePath(keypad, stx-1, sty, edx, edy)
        t = [">" + s for s in t]
        path.extend(t)

    if sty < edy and sty+1 < len(keypad) and stx < len(keypad[sty+1]):
        t = MakePath(keypad, stx, sty+1, edx, edy)
        t = ["v" + s for s in t]
        path.extend(t)
    elif sty > edy and sty-1 >= 0 and stx < len(keypad[sty-1]):
        t = MakePath(keypad, stx, sty-1, edx, edy)
        t = ["^" + s for s in t]
        path.extend(t)

    return path


def FillPaths(keypad, keypad_dir):
    for sty in range(len(keypad)):
        for stx in range(len(keypad[sty])):
            for edy in range(len(keypad)):
                for edx in range(len(keypad[edy])):
                    key = keypad[sty][stx] + keypad[edy][edx]
                    keypad_dir[key] = MakePath(keypad, stx, sty, edx, edy)

FillPaths(num_keypad, num_keypad_paths)
FillPaths(dir_keypad, dir_keypad_paths)
                    


cache = {}

def MakeMov(paths, code):
    if len(code) < 2:
        # starting on "A"
        return ["A"]
    if code in cache:
        return cache[code]
    moves = MakeMov(paths, code[1:])
    m = paths[code[0:2]]
    moves = [s1+s2 for s1 in moves for s2 in m]
    cache[code] = moves
    return moves


# starting on "A"
codes = ["A"+s for s in  readfile()]

res = 0
for code in codes:
    nb = int(''.join([str(x) for x in findNums(code)]))
    print(">>>>>", code)
    print("num part:", nb)

    moves = MakeMov(num_keypad_paths, code)
    for _ in range(2):
        nmoves = []
        for m in moves:
            nmoves.extend(MakeMov(dir_keypad_paths, m))
        moves = nmoves
        pp.pprint(moves)
    # removing starting "A"
    moves = [m[1:] for m in moves]

    lens = min([len(x) for x in moves])
    min_move = list(filter(lambda x: len(x) == lens, moves))[0]
    pp.pprint(min_move)
    print("len min_move:", len(min_move))

    cplx = len(min_move) * nb
    print("complexity:", cplx)
    print("")
    res += cplx

print("")
print("TOTAL COMPLEXITY:", res)



