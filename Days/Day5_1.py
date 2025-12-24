inputRaw: list = []

with open("Days/Day5.txt", encoding="utf-8") as file:
    for line in file:
        line = line.strip()
        inputRaw.append(line)

index = inputRaw.index("")
inputFresh: list = inputRaw[:index]  # 12-54, 43-123
inputIngredients: list[int] = [int(x)for x in inputRaw[index+1:]]
ranges: list[tuple[int, int]] = [(int(a), int(b))
                                 for a, b in (s.split("-", 1) for s in inputFresh)]

ranges.sort(key=lambda x: x[0])


freshIngredients = 0
for i in inputIngredients:
    print(f"Ingredient: {i}")
    for x, y in ranges:
        if i >= x and i <= y:
            print(f"Range: {x}-{y}")
            freshIngredients += 1
            break

print(freshIngredients)
