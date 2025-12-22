### Init required variables ###

grid:   list[list[int]] = []

### Read file in corresponding structure ###
with open("Days/Day3.txt") as file:
    for row in file:
        row = row.strip()
        if not row:
            continue
        grid.append([int(ch) for ch in row])

joltageSum = 0

for row in grid:
    passwordLength: int = 12
    joltage: list[str] = []
    index: int = 0
    lastIndex: int = 0
    validRow = row
    for i in range(passwordLength):
        passwordLength -= 1
        if passwordLength <= 0:
            validRow = row[lastIndex:]
        else:
            validRow = row[lastIndex:-passwordLength]
        maxVal = max(validRow)
        index = validRow.index(maxVal)
        lastIndex += index + 1
        joltage.append(str(maxVal))
    joltageSum += int("".join(joltage))

print(joltageSum)
