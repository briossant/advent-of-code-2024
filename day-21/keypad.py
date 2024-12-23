from libaoc import *
import pprint as pp

num_keypad_paths = {}
num_keypad = ["987", "654", "321", "A0"]

dir_keypad_paths = {}
dir_keypad = ["A^", ">v<"]


class Tree:
    def __init__(self, data):
        self.children = {}
        self.ln = len(data)
        self.data = data

        data = "A" + data
        self.split = [data[i-1:i+1] for i in range(1, len(data))]
        self.has_children = False
        self.is_cache_original = False
        self.depth = 0


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


Cache = {}
CacheAux = {}
ST_DEPTH = 26

def MakeMoveAux(paths, seg, depth):
    if seg+str(depth) in CacheAux:
        return CacheAux[seg+str(depth)]
    min_len = -1
    for m in paths[seg]:
        ln = MakeMov(m, depth-1)
        if min_len == -1 or ln < min_len:
            min_len = ln
    CacheAux[seg+str(depth)] = min_len
    return min_len

def MakeMov(moves, depth):
    if depth == 0:
        return len(moves)
    if moves+str(depth) in Cache:
        return Cache[moves+str(depth)]
    paths = num_keypad_paths if depth == ST_DEPTH else dir_keypad_paths
    moves = "A" + moves
    tt_len = 0
    for i in range(1, len(moves)):
        tt_len += MakeMoveAux(paths, moves[i-1:i+1], depth) 
    Cache[moves+str(depth)] = tt_len
    return tt_len 

codes = readfile()

res = 0
for code in codes:
    nb = int(''.join([str(x) for x in findNums(code)]))
    print(">>>>>", code)
    print("num part:", nb)

    ln = MakeMov(code, ST_DEPTH)

    print("len min_move:", ln)

    cplx = ln * nb
    print("complexity:", cplx)
    print("")
    res += cplx

print("")
print("TOTAL COMPLEXITY:", res)
