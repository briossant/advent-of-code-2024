from libaoc import *

lines = readfile()

regA = findNums(lines[0])[0]
regB = findNums(lines[1])[0]
regC = findNums(lines[2])[0]

program = findNums(lines[4])

program_ptr = 0


def getComboOp(op_code):
    match op_code:
        case 4:
            return regA
        case 5:
            return regB
        case 6:
            return regC
    return op_code


out = ""

while program_ptr < len(program):
    op = program[program_ptr+1]
    op_combo = getComboOp(op)
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

print(out)
