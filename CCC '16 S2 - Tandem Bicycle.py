t = int(input())  # type of operation (1 or 2)
n = int(input())
dmoj = sorted(list(map(int, input().split())))  # sorted integer values from input
peg = sorted(list(map(int, input().split())))

if t == 1:
    pairs = list(zip(dmoj, peg))
    print(sum([max(i) for i in pairs]))
else:
    peg.reverse()
    pairs = list(zip(dmoj, peg))
    print(sum([max(i) for i in pairs]))