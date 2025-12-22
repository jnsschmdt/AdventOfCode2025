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
        length = len(str(i))
        for j in range(1, round(len(str(i)) / 2) + 1):
            if length % j == 0:
                subString = str(i)[:j]
                pattern = rf"^(?:{re.escape(subString)})+$"

                if bool(re.fullmatch(pattern, str(i))):
                    result += i
                    break

print(f"Result: {result}")
