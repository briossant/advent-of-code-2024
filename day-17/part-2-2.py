from libaoc import *

lines = readfile()

# ordre de grandeur de regA - pas de bruteforce possible;
# iregA = 100000000000000
iregA = 0
iregB = findNums(lines[1])[0]
iregC = findNums(lines[2])[0]

program = findNums(lines[4])


def runProgram(regA, regB):
    i = 0
    while True:
        regB = (regA % 8) ^ 1
        regB = (regB ^ (regA // pow(2, regB))) ^ 4
        regA //= 8
        if regB % 8 != program[i]:
            return False, i, program[i], regB % 8
        i += 1
        if regA == 0:
            return i == len(program)


regAmin = 1
regAmax = 7
for i in range(1, len(program)):
    regAmin *= 8
    regAmax *= 8 + 7

print(regAmin)
print(regAmax)


def getRegB(regA):
    regB = (regA % 8) ^ 1
    regB = (regB ^ (regA // pow(2, regB))) ^ 4
    return regB


# program = [0, 3, 5, 4, 3, 0]
regA = [0]
for i in range(len(program)-1, -1, -1):
    nregA = []
    for x in range(len(regA)):
        good = False
        for j in range(0, 8):
            nA = regA[x] + j
            if getRegB(nA) % 8 == program[i]:
                good = True
                nregA.append(nA*8)
    print(', '.join([str(x) for x in nregA]))
    print(i, program[i])
    regA = nregA

print(regA)
for rA in regA:
    print(rA, runProgram(rA, 0))
    print(rA, runProgram(rA//8, 0))

print("min", min(regA)//8)

exit(0)
for mm in regA:
    print("###########################")
    mmm = mm - 10000000
    mmmm = mm + 10000000
    while not runProgram(mmm, 0) and mmm < mmmm:
        mmm += 1
        if mmm % 10000 == 0:
            print(mmm)
    if mmm < mmmm:
        print("RES", mmm-1)
        break
