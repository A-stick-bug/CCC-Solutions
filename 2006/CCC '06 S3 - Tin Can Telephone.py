# First, we represent each building as line segments of the sides
# Then, we can use geometry to check if anyy line segment in the building intersects with p1-p2
# Time complexity: O(n), check for intersection with every other line


def batch_points(arr):
    """group every 2 elements together into a tuple pair that represent point (x,y)"""
    return [(arr[i], arr[i + 1]) for i in range(0, len(arr), 2)]


# thanks to stack overflow: https://stackoverflow.com/questions/3838329/how-can-i-check-if-two-segments-intersect
def intersects(a, b):
    p = [b[0][0] - a[0][0], b[0][1] - a[0][1]]
    q = [a[1][0] - a[0][0], a[1][1] - a[0][1]]
    r = [b[1][0] - b[0][0], b[1][1] - b[0][1]]

    t = (q[1] * p[0] - q[0] * p[1]) / (q[0] * r[1] - q[1] * r[0]) \
        if (q[0] * r[1] - q[1] * r[0]) != 0 \
        else (q[1] * p[0] - q[0] * p[1])
    u = (p[0] + t * r[0]) / q[0] \
        if q[0] != 0 \
        else (p[1] + t * r[1]) / q[1]

    return 0 <= t <= 1 and 0 <= u <= 1


inf = 1 << 30
p1, p2 = batch_points(list(map(int, input().split())))  # check if line segment p1-p2 intersect with anything

# each building can be represented as the lines of each edge
buildings = int(input())
total = 0

for _ in range(buildings):
    lines = []
    points = batch_points(list(map(int, input().split()))[1:])
    for i in range(len(points)):
        lines.append((points[i], points[i - 1]))

    # check if any building line intersect with p1-p2
    total += any(intersects((p1, p2), line) for line in lines)

print(total)
