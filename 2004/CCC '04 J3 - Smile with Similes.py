adj_n = int(input())
noun_n = int(input())

adj = []
noun = []

i = 0
while i < adj_n:
    x = str(input())
    adj.append(x)
    i += 1

i = 0
while i < noun_n:
    x = str(input())
    noun.append(x)
    i += 1

for a in adj:
    for n in noun:
        print(f"{a} as {n}")