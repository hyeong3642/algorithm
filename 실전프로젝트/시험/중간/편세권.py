t = int(input())
for i in range(t):
    n, c = map(int, input().split())
    cvs = []
    for i in range(c):
        x, y = map(int, input().split())
        cvs.append((x,y))
    max = 0
    x, y = 0,0
    for i in range(0,n):
        for j in range(0,n):
            score =0
            if (i, j) in cvs:
                continue
            for c in cvs:
                dist = abs(c[0]-i) + abs(c[1]-j)
                if dist <=10:
                    score +=1
                if dist <=3:
                    score +=2
            if score > max:
                x = i
                y = j
                max = score
    print(x,y,max)