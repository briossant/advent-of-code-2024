from libaoc import *

lines = readfile()

towels = lines[0].split(", ")

patterns = lines[2:]

Cache = {}


def match(pattern):
    if len(pattern) == 0:
        return True
    if pattern in Cache:
        return Cache[pattern]
    for tow in towels:
        if len(pattern) >= len(tow) and tow == pattern[0:len(tow)]:
            if match(pattern[len(tow):]):
                Cache[pattern] = True
                return True
    Cache[pattern] = False
    return False


ct = 0
for pat in patterns:
    if match(pat):
        ct += 1

print("matches:", ct)
