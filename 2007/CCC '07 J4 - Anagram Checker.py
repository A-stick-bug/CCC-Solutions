# looking back at my horribly inefficient solution bothered me, so I improved it
# now, it's O(n)

from collections import defaultdict

# if they have the same amount of each letter, they are anagrams
s1 = input()
s2 = input()

count1 = defaultdict(int)
for i in s1:
    if i != " ":  # ignore spaces
        count1[i] += 1

count2 = defaultdict(int)
for i in s2:
    if i != " ":
        count2[i] += 1

if count1 == count2:
    print("Is an anagram.")
else:
    print("Is not an anagram.")
