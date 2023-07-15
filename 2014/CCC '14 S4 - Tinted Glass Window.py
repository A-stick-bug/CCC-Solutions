n = int(input())
threshold = int(input())
x_coords = []
y_coords = []

for i in range(n):
    # read the coordinates and tint-factor of each piece of glass
    x1,y1,x2,y2,tint = map(int, input().split())
    x_coords.append([x1, y1, y2, tint])  # [x1, y1, x2, tint]
    x_coords.append([x2, y1, y2, -tint]) # [x2, y1, x2, -tint]
    y_coords.append(y1)
    y_coords.append(y2)

x_coords = sorted(x_coords)
y_coords = sorted(list(set(y_coords)))

nums = [0 for x in range(len(y_coords) - 1)]
size = len(nums)
lx = 0
res = 0

for i in x_coords:
    for j in range(size):
        if nums[j] >= threshold:
            res += (y_coords[j + 1] - y_coords[j]) * (i[0] - lx)

    # overlap
    for j in range(size):
        if i[1] <= y_coords[j] and i[2] >= y_coords[j + 1]:
            nums[j] += i[3]
    lx = i[0]

print(res)