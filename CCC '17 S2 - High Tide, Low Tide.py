n = int(input())
arr = input().split()
arr = [int(i) for i in arr]
arr.sort()

lowest = None
res = []
if n % 2 != 0:
    # is odd
    lowest = arr.pop(0)

mid = n // 2

# first to mid inclusive is smaller values
# mid + 1 to end of arr inclusive is larger values, bring those values together
lower = mid - 1
while lower >= 0:
    res.append(arr[lower])
    res.append(arr[mid])
    lower -= 1
    mid += 1

if lowest:
    res.append(lowest)
print(*res, sep=" ")
