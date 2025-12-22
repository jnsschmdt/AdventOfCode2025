### Init Helper Objects ###
commands:           list[str] = []
pointer:      int = 50
onZeroCounter:      int = 0
overZeroCounter:    int = 0

### Read Puzzle Input ###
with open("Days/Day1.txt") as f:
    for r in f:
        commands.append(r.strip())

### Iterate over commands###
for c in commands:
    direction:      str = c[0]
    value:          int = int(c[1:])
    factor:         int = int(c[1:])//100
    prevPointer:    int = pointer

    overZeroCounter += factor

    if direction == "R":
        pointer += int(c[1:]) % 100
    else:
        pointer -= int(c[1:]) % 100

    if (pointer < 0):
        pointer += 100
        if (prevPointer > 0):
            overZeroCounter += 1
    elif (pointer > 100):
        pointer -= 100
        if (prevPointer > 0):
            overZeroCounter += 1
    elif (pointer == 0):
        onZeroCounter += 1
    elif (pointer == 100):
        onZeroCounter += 1
        pointer -= 100

print(f"Final Result: {onZeroCounter + overZeroCounter}")
