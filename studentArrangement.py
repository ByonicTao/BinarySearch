data = input().split()
N = int(data[0])
M = int(data[1])
K = int(data[2])
A = input().split()

nonPref = 0

rows = [K for i in range(M)]


def findNextRow(currentRow, rows):
    if(currentRow == len(rows)):
        next = 0
    else:
        next = currentRow + 1
    while (next != currentRow):
        if(next == len(rows)):
            next = 0
        if(rows[next] > 0):
            return next
        else: next += 1
    return -1

for student in A:
    if (rows[int(student) - 1] > 0):
        rows[int(student) - 1] -= 1
    else:
        nonPref += 1
        next = findNextRow(int(student) - 1, rows)
        if (next > 0):
            rows[next] -= 1

print(nonPref)
