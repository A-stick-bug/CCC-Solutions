from collections import defaultdict

same = defaultdict(set)
for _ in range(int(input())):
    a,b = input().split()
    same[a].add(b)

different = defaultdict(set)
for _ in range(int(input())):
    a,b = input().split()
    different[a].add(b)

res = 0

# note: constraint can't be violated twice, so we remove it after being violated
for _ in range(int(input())):
    abc = input().split()
    for x in abc:
        to_remove = set()
        for s in same[x]:
            if s not in abc:
                to_remove.add(s)
                res += 1
        same[x] -= to_remove  # remove after iterating because you can't remove while iterating over a set

        to_remove = set()
        for p in abc:
            if p != x and p in different[x]:
                to_remove.add(p)
                res += 1
        same[x] -= to_remove

print(res)
