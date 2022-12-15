def rotate(image):
    n = len(image)
    rot = [[0] * n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            rot[c][n-1-r] = image[r][c]
    return rot