"""
https://dmoj.ca/problem/ccc24j4
Using logic reasoning and a bit of implementation

Note the following:
- "Alex never actually tries to type the wrong letter displayed by the silly key"
- "Alex presses the silly key at least once"
Using these 2 statements, we can reason that the character that only exists in the second string must
be the result of the silly key

Note that we add a common letter at the end of both strings to avoid handling cases like the quiet key being at the end.
"""

s = input() + "."  # original string
t = input() + "."  # resulting string

quiet = '-'
silly = ['-', '-']  # [original character, resulting character]

for c in "qwertyuiopasdfghjklzxcvbnm":  # find the result of the silly key
    if c in t and c not in s:
        silly[1] = c

i = j = 0
while i < len(s) and j < len(t):
    if s[i] == t[j]:  # same letter, don't do anything
        i += 1
        j += 1
        continue

    if t[j] == silly[1]:  # result is silly key, s[i] must be the original character then
        silly[0] = s[i]
        i += 1
        j += 1

    else:  # result is NOT the silly key, it must be the quiet key then
        quiet = s[i]
        i += 1  # only increment i since the quiet key doesn't result in any characters being typed

print(*silly)
print(quiet)
