"""
Important: Alex never presses the silly key immediately after pressing the quiet key
"""

s = input() + "."
t = input() + "."

quiet = '-'
silly = ['-', '-']

i = j = 0
while i < len(s) and j < len(t):
    if s[i] == t[j]:
        i += 1
        j += 1
        continue

    if s[i] == quiet:
        i += 1

    elif s[i + 1] == t[j]:  # skipped a letter
        quiet = s[i]
        i += 1

    else:  # replaced a letter
        silly[0] = s[i]
        silly[1] = t[j]
        i += 1
        j += 1

print(*silly)
print(quiet)
