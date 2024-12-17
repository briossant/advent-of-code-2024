from libaoc import *

lines = readfile()

# ordre de grandeur de regA - pas de bruteforce possible;
# iregA = 100000000000000
iregA = 0
iregB = findNums(lines[1])[0]
iregC = findNums(lines[2])[0]

program = findNums(lines[4])


def getComboOp(op_code, regA, regB, regC):
    match op_code:
        case 4:
            return regA
        case 5:
            return regB
        case 6:
            return regC
    return op_code


def runProgram(regA, regB, regC):

    program_ptr = 0

    out = ""

    while program_ptr < len(program):
        op = program[program_ptr+1]
        op_combo = getComboOp(op, regA, regB, regC)
        match program[program_ptr]:
            case 0:
                regA //= pow(2, op_combo)
            case 1:
                regB = regB ^ op
            case 2:
                regB = op_combo % 8
            case 3:
                if regA != 0:
                    program_ptr = op
                    continue
            case 4:
                regB = regB ^ regC
            case 5:
                if len(out) > 0:
                    out += ","
                out += str(op_combo % 8)
            case 6:
                regB = regA // pow(2, op_combo)
            case 7:
                regC = regA // pow(2, op_combo)
        program_ptr += 2

    return out


rp_og = ','.join([str(x) for x in program])

while True:
    rp = runProgram(iregA, iregB, iregC)
    print(iregA, rp)
    if rp_og == rp:
        print("res " + str(iregA))
        break
    iregA += 1
