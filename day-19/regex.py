from libaoc import *
import re2 as re

lines = readfile()

towels = lines[0].split(", ")
patterns = lines[2:]

reg = re.compile('(' + '|'.join(towels) + ')*')
matches = len(list(filter(lambda pat: re.fullmatch(reg, pat), patterns)))

print("matches:", matches)
