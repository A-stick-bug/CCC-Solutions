# 14/15 TLE

same = []
different = []

repeats1 = int(input())

# must be in same group
for _ in range(repeats1):
    to_add = input().split()
    same.append(to_add)

repeats2 = int(input())

# must be in different group
for _ in range(repeats2):
    to_add2 = input().split()
    different.append(to_add2)

print(f"same constraints: {same}")
print(f"different constraints: {different}")

repeats3 = int(input())
broke = 0

for _ in range(repeats3):
    group = input().split()
    for i in same.copy():
        if (i[0] in group or i[1] in group) and not (i[0] in group and i[1] in group):
            broke += 1
            print("+1")
            same.remove(i)

    for i in different.copy():
        if i[0] in group and i[1] in group:
            broke += 1
            print("+1")
            different.remove(i)

print(broke)
