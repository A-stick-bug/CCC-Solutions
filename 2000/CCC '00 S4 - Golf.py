clubs = []
length = int(input())
club_count = int(input())

for i in range(club_count):
    clubs.append(int(input()))

def find_min(arr, target):
    n = len(arr)
    dp = [float('inf')] * (target+1)
    dp[0] = 0
    for i in range(1, target+1):
        for j in range(n):
            if arr[j] <= i:
                dp[i] = min(dp[i], dp[i-arr[j]] + 1)
    return dp[target] if dp[target] != float('inf') else -1


min_val = find_min(clubs,length)
print(f"Roberta wins in {min_val} strokes.") if min_val!=-1 else print("Roberta acknowledges defeat.")
