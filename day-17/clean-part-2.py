from libaoc import *

lines = readfile()
program = findNums(lines[4])


def getRegB(regA):
    regB = (regA % 8) ^ 1
    regB = (regB ^ (regA // pow(2, regB))) ^ 4
    return regB


regA = [0]
for i in range(len(program)-1, -1, -1):
    nregA = []
    for x in range(len(regA)):
        for j in range(0, 8):
            nA = regA[x] + j
            if getRegB(nA) % 8 == program[i]:
                nregA.append(nA*8)
    regA = nregA

print("RES", min(regA)//8)
