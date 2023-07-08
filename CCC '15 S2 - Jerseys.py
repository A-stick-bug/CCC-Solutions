# unique solution, read comments for details
# in Java, compareTo can be used

j = int(input())
athletes = int(input())

jerseys = {}

for i in range(1,j+1):
    jerseys[i] = input()

count = 0
for i in range(athletes):
    size,num = input().split()
    num = int(num)
    # uses the fact that S > M > L in ascii
    if jerseys[num] < size or jerseys[num] == size:
        count += 1
        jerseys[num] = "a"  # smaller than S, M, and L in ascii

print(count)
