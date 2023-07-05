code = [input().split() for _ in range(int(input()))]
code.sort(key=lambda i:i[1], reverse=True)  # sort by length of encoding, always use the longest available encoding

encoded = input()
res = ""
while encoded:
    for letter, bits in code:
        if encoded.startswith(bits):
            res += letter
            encoded = encoded[len(bits):]
            break

print(res)
