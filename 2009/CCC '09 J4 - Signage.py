# annoying string/array processing

width = int(input())
s = "WELCOME TO CCC GOOD LUCK TODAY".split()

l = [len(word) for word in s]
req = [len(s[0])]
for i in range(1, len(s)):
    req.append(len(s[i]) + 1)  # +1 because a space is needed

total = 0
segments = [[]]
i = 0
while i < len(req):
    if total + req[i] > width:  # need a new line
        total = 0
        segments.append([])
        req[i] -= 1  # no need to have a space before the word because it is a new line
        continue
    total += req[i]
    segments[-1].append(s[i])
    i += 1

# fill in the dots
for words in segments:
    if len(words) == 1:  # edge case for line with only 1 word
        print(words[0] + "." * (width - len(words[0])))
        continue

    separator = '.'
    total_length = sum(len(word) for word in words)
    gaps = len(words) - 1
    seperator_count = width - total_length
    separators_per_gap, extras = divmod(seperator_count, gaps)
    res = ''

    for i, word in enumerate(words):
        res += word
        if i < gaps:
            res += separator * separators_per_gap
            if i < extras:  # the ones on the left with an extra dot
                res += separator
    print(res)


# solution 2
def format_sign(width):
    message = "WELCOME TO CCC GOOD LUCK TODAY"
    words = message.split()
    lines = []
    line = []
    line_length = 0

    for word in words:
        if line_length + len(word) + len(line) <= width:
            line.append(word)
            line_length += len(word)
        else:
            lines.append(line)
            line = [word]
            line_length = len(word)
    lines.append(line)

    for line in lines:
        if len(line) == 1:
            print(line[0])
        else:
            spaces = width - sum(len(word) for word in line)
            gaps = len(line) - 1
            space_per_gap, extra_spaces = divmod(spaces, gaps)
            for i, word in enumerate(line):
                print(word, end="")
                if i < gaps:
                    print("." * space_per_gap, end="")
                    if i < extra_spaces:
                        print(".", end="")
            print()
