### Init required variables ###

grid:   list[list[int]] = []
result: int = 0

### Read file in corresponding structure ###
with open("Days/Day3_test.txt") as file:
    for row in file:
        row = row.strip()
        if not row:
            continue
        grid.append([int(ch) for ch in row])

### main logic ###
for row in grid:
    maxVal: int = max(row[:-1])
    for col in range(len(row) - 1):
        valFirst = row[col]
        if valFirst == maxVal:
            valSecond = max(row[col+1:])
            val = int(f"{valFirst}{valSecond}")
    result += val

### print answer ###
print(result)
