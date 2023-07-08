normal = input()
encrypted = input()
to_decrypt = input()

map = {}
for i in range(len(normal)):
    map[encrypted[i]] = normal[i]

output = ""
for i in range(len(to_decrypt)):
    if to_decrypt[i] in map.keys():
        output+=map[to_decrypt[i]]
    else:
        output+="."

print(output)