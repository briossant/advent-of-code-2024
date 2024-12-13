file = open("input.txt", "r")

reports = file.readlines()
reports = [[int(x) for x in l.split(" ")] for l in reports]


def is_safe(report):
    if len(report) <= 1:
        return True
    if report[0] >= report[1]:
        report.reverse()
    for i in range(1, len(report)):
        if report[i-1] >= report[i]:
            return False
        if report[i] - report[i-1] > 3:
            return False
    return True


safe_count = sum([is_safe(x) for x in reports])
print("number of safe reports: " + str(safe_count))

# part 2


def is_decending(report):
    dec_count = 0
    for i in range(1, len(report)):
        if report[i] < report[i-1]:
            dec_count += 1
    return dec_count >= 2


def check_levels(l1, l2):
    if l1 >= l2 or l2 - l1 > 3:
        return False
    return True


def is_safe_tolerant(report):
    if len(report) <= 2:
        return True
    if is_decending(report):
        report.reverse()
    tolerence = False
    for i in range(1, len(report)):
        if not check_levels(report[i-1], report[i]):
            if tolerence:
                return False
            if i < len(report) - 1 and check_levels(report[i-1], report[i+1]):
                report[i] = report[i-1]
            elif i > 1 and not check_levels(report[i-2], report[i]):
                report[i] = report[i-1]
            tolerence = True
    return True


safe_count = sum([is_safe_tolerant(x) for x in reports])
print("number of safe reports with tolerance: " + str(safe_count))
