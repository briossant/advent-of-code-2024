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
        self.split = [data[i-1:i+1] for i in range(1,len(data))]
        self.has_children = False

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
                    

def MakeMov(paths, tree):
    if not tree.has_children:
        tt_ln = 0
        for sp in tree.split:
            tree.children[sp] = [Tree(s) for s in paths[sp]]
            tt_ln += tree.children[sp][0].ln
        tree.ln = tt_ln
        tree.has_children = True
        return tt_ln

    tt_ln = 0
    for sp in tree.split:
        min_ln = -1
        nc = []
        for child in tree.children[sp]:
            ln = MakeMov(paths, child)
            if min_ln == -1 or ln < min_ln:
                min_ln = ln
                nc = [child]
            elif ln == min_ln:
                nc.append(child)
        tree.children[sp] = nc
        tt_ln += min_ln
    tree.ln = tt_ln
    return tt_ln



codes = readfile()

res = 0
for code in codes:
    nb = int(''.join([str(x) for x in findNums(code)]))
    print(">>>>>", code)
    print("num part:", nb)
    
    tree = Tree(code)
    MakeMov(num_keypad_paths, tree)
    for _ in range(10):
        MakeMov(dir_keypad_paths, tree)

    ln = tree.ln

    print("len min_move:", ln)

    cplx = ln * nb
    print("complexity:", cplx)
    print("")
    res += cplx

print("")
print("TOTAL COMPLEXITY:", res)



