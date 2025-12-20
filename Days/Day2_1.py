import re

ids: list[tuple[int, int]] = []
result = 0

with open("Days/Day2.txt") as f:
    for r in f:
        r = r.strip()
        tuples = r.split(",")
        for t in tuples:
            try:
                t1, t2 = t.split("-")
                ids.append((int(t1), int(t2)))
            except Exception as e:
                print(f"Error: {e}")
                print(f"Error Object: {t}")

for id in ids:
    for i in range(id[0], (id[1] + 1)):
        idAsString = str(i)
        length = len(idAsString)
        if length%2 == 0: 
            left, right = idAsString[:length//2], idAsString[length//2:]
            if left == right: result += i

print(f"Result: {result}")