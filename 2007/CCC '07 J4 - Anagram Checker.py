# looking back at my horribly inefficient solution bothered me, so I improved it
# now, it's O(n)


# O(n*log(n)), one liner solution for fun :)
# somehow faster than the O(n) solution because the test cases are too small
# print("Is an anagram." if sorted(input().replace(" ", "")) == sorted(input().replace(" ", "")) else "Is not an anagram.")


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
