import sys

input = sys.stdin.readline  # fast input

n = int(input())
scores = [int(input()) for _ in range(n)]
unique = sorted(set(scores))  # sort scores and remove duplicates

# get third-highest score and the number of times it appears
print(unique[-3], scores.count(unique[-3]))

