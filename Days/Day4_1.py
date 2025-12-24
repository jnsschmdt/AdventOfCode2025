grid: list[list[str]] = []

with open("Days/Day4.txt", encoding="utf-8") as file:
    for line in file:
        line = line.strip()
        if not line:
            continue
        grid.append(list(line))

operations: list[tuple[int, int]] = [
    (-1, +1), (0, +1), (+1, +1),
    (-1, 0),           (+1, 0),
    (-1, -1), (0, -1), (+1, -1)
]

width = len(grid[0])
height = len(grid)
balesAccessable = 0


def isValidField(width: int, height: int, row: int, col: int) -> bool:
    return 0 <= row < height and 0 <= col < width


def baleCanBeAccessed(width: int, height: int, row: int, col: int) -> bool:
    balesAround = 0
    for dr, dc in operations:
        rr = row + dr
        cc = col + dc
        if isValidField(width, height, rr, cc) and grid[rr][cc] == "@":
            balesAround += 1
    return balesAround < 4


print(f"Dimensions: h:{height} w:{width}")

for row in range(height):
    for col in range(width):
        if grid[row][col] == "@":
            accessable = baleCanBeAccessed(width, height, row, col)
            print(f"Field: grid[{row}][{col}] accessable: {accessable}")
            if accessable:
                balesAccessable += 1

print(f"Bales Accesable: {balesAccessable}")
