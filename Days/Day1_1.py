### Init Helper Objects ###
commands: list[str] = []
pointer: int = 50
onZeroCounter: int = 0

### Read Puzzle Input ###
with open("Days/Day1.txt") as f:
    for r in f:
        commands.append(r.strip())

for c in commands:
    direction:  int = c[0]
    value:      int = c[1:]

    print("-"*20)
    print(f"Pointer: {pointer}")
    print(f"Direction: {direction}")
    print(f"Value: {value}")

    if direction == "R":
        pointer += int(c[1:]) % 100
    else:
        pointer -= int(c[1:]) % 100

    print(f"Result: {pointer}")

    if (pointer < 0):
        pointer += 100
    elif (pointer >= 100):
        pointer -= 100

    if (pointer == 0):
        onZeroCounter += 1
        print(f"onZeroCounter: {onZeroCounter}")

print("-"*20)
print(f"Final Result: {onZeroCounter}")
