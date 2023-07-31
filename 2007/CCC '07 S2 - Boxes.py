# 15/15
# low constraints so brute force, O(mn)
# a lot of sorting

n = int(input())

# note: we sort the dimensions so that we can tell if an item fits in it more easily
boxes = [sorted(map(int, input().split())) for _ in range(n)]
boxes.sort(key=lambda box: box[0] * box[1] * box[2])  # sort by volume, as question asks for the smallest box that fits

for i in range(int(input())):
    dimensions = sorted(map(int, input().split()))
    for box in boxes:
        fits = True
        for i in range(3):  # make sure the box is smaller in all 3 dimensions
            if dimensions[i] > box[i]:
                fits = False

        if fits:  # found a box that fits so print its volume
            print(box[0] * box[1] * box[2])
            break

    if not fits:  # didn't find a box that fits this item
        print("Item does not fit.")
