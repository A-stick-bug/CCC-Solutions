# method is correct but TLE because python is too slow
# O(n*log(n))

class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)

    def update(self, i, diff):
        while i <= self.size:
            self.tree[i] += diff
            i += i & -i

    def select(self, k):  # "traversal" in log(n)
        i = 0
        log2 = self.size.bit_length()  # log2(self.size), number of bits needed to represent self.size
        for power in reversed(range(log2)):
            # 1<<x = 2 to the power of x
            if i + (1 << power) <= self.size and self.tree[i + (1 << power)] < k:
                i += 1 << power
                k -= self.tree[i]
        return i + 1


n = int(input())
queries = []
scores = set()
for _ in range(n):
    q = input().split()
    if q[0] != "Q":
        scores.add(int(q[2]))  # get unique scores
    queries.append(q)

scores = sorted(scores, reverse=True)  # sort in reverse because rank 1 has HIGHEST score
compress = {val: i + 1 for i, val in enumerate(scores)}  # 1-indexed ranks

rtp = {}  # maps a ranking to a person
ptr = {}  # map a person to their ranking

bit = FenwickTree(len(scores) + 1)
for q in queries:
    if q[0] == "Q":
        k_th_rank = bit.select(int(q[1]))
        person = rtp[k_th_rank]
        print(person)

    elif q[0] == "N":
        person, score = map(int, q[1:])
        rank = compress[score]
        rtp[rank] = person
        ptr[person] = rank
        bit.update(rank, 1)

    elif q[0] == "M":
        person, score = map(int, q[1:])
        new_rank = compress[score]
        bit.update(ptr[person], -1)  # remove current rank
        bit.update(new_rank, 1)
        ptr[person] = new_rank
        rtp[new_rank] = person
