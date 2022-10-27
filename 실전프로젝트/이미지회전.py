t= int(input())

def rotate(n, image):
    rot = [[0] * n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            rot[c][n-1-r] = image[r][c]
    return rot

for i in range(t):  
    n, a= map(int, input().split())
    image = []
    for i in range(n):
        image.append(input())
    if a == 90 or a== -270:
        ans = rotate(n, image)
        for i in range(len(image)):
            tmp = ''
            for j in range(len(image)):
                tmp += ans[i][j]
            print(tmp)
    elif a == 180 or a == -180 :
        ans = rotate(n,rotate(n, image))
        for i in range(len(image)):
            tmp = ''
            for j in range(len(image)):
                tmp += ans[i][j]
            print(tmp)
    elif a== 270 or a== -90:
        ans = rotate(n,rotate(n,rotate(n, image)))
        for i in range(len(image)):
            tmp = ''
            for j in range(len(image)):
                tmp += ans[i][j]
            print(tmp)
    else:
        for i in range(len(image)):
            tmp = ''
            for j in range(len(image)):
                tmp += image[i][j]
            print(tmp)


