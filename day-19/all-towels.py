from libaoc import *

lines = readfile()

towels = lines[0].split(", ")

patterns = lines[2:]

Cache = {}


def match(pattern):
    if len(pattern) == 0:
        return 1
    if pattern in Cache:
        return Cache[pattern]
    res = 0
    for tow in towels:
        if len(pattern) >= len(tow) and tow == pattern[0:len(tow)]:
            res += match(pattern[len(tow):])
    Cache[pattern] = res
    return res


ct = 0
for pat in patterns:
    ct += match(pat)

print("matches:", ct)
