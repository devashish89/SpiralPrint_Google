array_2d = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

top = 0
bottom = len(array_2d) - 1
left = 0
right = len(array_2d[0]) - 1

while left <= right and top <= bottom:
    for r in range(top, bottom + 1, 1):
        print(array_2d[r][left])

    left += 1

    for c in range(left, right + 1, 1):
        print(array_2d[bottom][c])

    bottom -= 1

    for r in range(bottom, top - 1, -1):
        print(array_2d[r][right])

    right -= 1

    for c in range(right, left - 1, -1):
        print(array_2d[top][c])

    top += 1
