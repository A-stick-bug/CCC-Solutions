a = input()
b = input()

alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet = alphabet.upper()

x = True

for i in alphabet:
    num_a = a.count(str(i))
    num_b = b.count(str(i))

    if int(num_a) != int(num_b):
        x = False
        break

if x:
    print("Is an anagram.")
else:
    print("Is not an anagram.")