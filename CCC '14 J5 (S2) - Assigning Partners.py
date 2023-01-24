# FIRST JUNIOR 5 PROBLEM SOLVED

length = int(input())
a = input().split()
b = input().split()

groups = {}
result = "good"

for i in range(length):
    if a[i] == b[i]:
        result = "bad"
        break
    if a[i] in groups or b[i] in groups:
        if a[i] in groups.keys():
            if groups[a[i]] != b[i]:
                result = "bad"
                break
        elif b[i] in groups.keys():
            if groups[b[i]] != a[i]:
                result = "bad"
                break
    else:
        groups[a[i]] = b[i]

print(result)