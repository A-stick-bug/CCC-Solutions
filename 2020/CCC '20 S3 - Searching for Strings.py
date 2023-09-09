import sys

# take input and create frequency arrays
needle = input()
ln = len(needle)
letters = [0] * 26  # any substring with the same letter frequency as this is an answer
for char in needle:
    letters[ord(char) - 97] += 1

haystack = input()
lh = len(haystack)

hashes = set()
if ln > lh:  # corner case: haystack is longer than needle
    print(0)
    sys.exit()

# compute the stuff for rolling hash
#######################
p = 29  # only a-z (26 letters) so this base is fine

# an alternate method is double hashing: hash with 2 different prime numbers
# when both hashes match another string's they are (probably) the same
mod = 177635683940025046467781066894531

# precompute the powers of p, so we can take the modulus and prevent overflow
power = [1] * (lh + 1)
for i in range(1, lh + 1):
    power[i] = (power[i - 1] * p) % mod

hash_values = [0] * (lh + 1)
for i in range(lh):
    hash_values[i + 1] = (hash_values[i] + (ord(haystack[i]) - 97 + 1) * power[i]) % mod
#######################

# handle the first substring seperately because we have to build the frequency array
freq = [0] * 26
for i in range(ln):
    freq[ord(haystack[i]) - 97] += 1

if letters == freq:
    current_hash = (hash_values[0 + ln] - hash_values[0] + mod) % mod
    current_hash = (current_hash * power[lh - 0 - ln]) % mod
    hashes.add(current_hash)

for i in range(1, lh - ln + 1):
    freq[ord(haystack[i-1]) - 97] -= 1  # slide substring window
    freq[ord(haystack[i + ln - 1]) - 97] += 1

    current_hash = (hash_values[i + ln] - hash_values[i] + mod) % mod
    current_hash = (current_hash * power[lh - i - ln]) % mod

    if letters == freq:
        hashes.add(current_hash)

print(len(hashes))
