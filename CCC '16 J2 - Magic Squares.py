arr = []

for i in range(4):
    x = input().split()
    arr.append(list(map(int,x)))

#print(arr)
value = sum(arr[0])
flag = True

for i in arr:
    if sum(i) != value:
        flag = False
        break

if flag:
    # verticals
    count = 0
    for j in range(4):
        count = 0
        for k in range(4):
            count += arr[k][j]

        if count != value:
            flag = False
            break

if flag:
    print("magic")
else:
    print("not magic")