# 15/15, just get the insert/pop positions right

n = int(input())
streams = [int(input()) for _ in range(n)]

while True:
    action = input()
    if action == "77":
        break

    elif action == "99":
        i = int(input()) - 1  # minus one because of 1-indexing
        left = int(input())/100
        right = 1 - left
        streams.insert(i+1, left*streams[i])
        streams.insert(i + 2, right*streams[i])
        streams.pop(i)

    elif action == "88":
        i = int(input()) - 1
        comb = streams[i] + streams[i + 1]
        streams.pop(i + 1)
        streams[i] = comb

print(*map(int, streams), sep=" ")
