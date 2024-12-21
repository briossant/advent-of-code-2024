import itertools as it
import pprint as pp

base = list('abbccc')
All = list(set(it.permutations(base)))


def cycle(s):
    s = list(s)
    for _ in range(len(base)-1):
        s.append(s.pop(0))
        All.remove(tuple(s))


m = len(All)
i = 0
while m/len(base) != len(All):
    cycle(All[i])
    i += 1


def Mirror(s):
    s = list(s)
    s.reverse()
    while not All.count(tuple(s)):
        s.append(s.pop(0))
    All.remove(tuple(s))


m = len(All)
i = 0
while m/2 != len(All):
    Mirror(All[i])
    i += 1

pp.pprint([''.join(a) for a in All])
