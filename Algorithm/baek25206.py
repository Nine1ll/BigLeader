import sys

score = [list(sys.stdin.readline().split()) for _ in range(20)]

credit = {"A+": 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0,
          "C+": 2.5, "C0": 2.0, "D+": 1.5, "D0": 1.0,
          "P": 0, "F": 0}

molecules = 0
denominator = 0

for i, lst in enumerate(score):
    if lst[-1] != "P":
        denominator += float(lst[1])
        molecules += credit[lst[-1]]*float(lst[1])

print(round(molecules/denominator, 6))
