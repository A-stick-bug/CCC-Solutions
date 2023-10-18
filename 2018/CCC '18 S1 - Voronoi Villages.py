n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort()

smallest = float('inf')
for i in range(1, n-1):
    smallest = min(smallest, (arr[i+1]-arr[i-1])/2)

print(round(smallest, 2))
