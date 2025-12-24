inputRaw: list = []

with open("Days/Day5.txt", encoding="utf-8") as file:
    for line in file:
        line = line.strip()
        inputRaw.append(line)

index = inputRaw.index("")
ranges: list[tuple[int, int]] = [(int(a), int(b))
                                 for a, b in (s.split("-", 1) for s in inputRaw[:index])]

ranges.sort(key=lambda x: x[0])


optimizedRanges: list[tuple[int, int]] = []

start, end = ranges[0]
for idx, (x, y) in enumerate(ranges[1:], start=1):
    # Kontakt / Überlappung (inkl. direktes Berühren bei inklusiven Intervallen)
    if x <= end + 1:
        end = max(end, y)
    else:
        optimizedRanges.append((start, end))
        start, end = x, y

optimizedRanges.append((start, end))
numbers = 0

for x, y in optimizedRanges:
    numbers += len(range(x, y + 1))

print(numbers)
